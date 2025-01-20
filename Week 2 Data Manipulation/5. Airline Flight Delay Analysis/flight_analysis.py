import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from datetime import datetime
import os

class FlightDelayAnalyzer:
    def __init__(self, data_path):
        """Initialize the analyzer with the flight data file path."""
        self.data_path = data_path
        self.df = None
        self.map_data = None
        
    def load_data(self):
        """Load and preprocess the flight data."""
        try:
            # First, let's see what columns we actually have
            print("Checking data file structure...")
            df_peek = pd.read_csv(self.data_path, nrows=1)
            print("\nAvailable columns in the file:")
            print(df_peek.columns.tolist())
            
            # Read the data
            print("\nLoading flight data...")
            self.df = pd.read_csv(self.data_path)
            
            # Process dates if FL_DATE exists
            print("Processing dates...")
            if 'FL_DATE' in self.df.columns:
                self.df['FL_DATE'] = pd.to_datetime(self.df['FL_DATE'])
                self.df['YEAR'] = self.df['FL_DATE'].dt.year
                self.df['MONTH'] = self.df['FL_DATE'].dt.month
                self.df['DAY'] = self.df['FL_DATE'].dt.day
            
            # Handle airport codes
            if 'ORIGIN' in self.df.columns and 'ORIGIN_AIRPORT' not in self.df.columns:
                self.df['ORIGIN_AIRPORT'] = self.df['ORIGIN']
            
            # Calculate total delay
            print("Calculating delays...")
            delay_columns = []
            if 'DEP_DELAY' in self.df.columns:
                delay_columns.append('DEP_DELAY')
            if 'ARR_DELAY' in self.df.columns:
                delay_columns.append('ARR_DELAY')
            
            if delay_columns:
                self.df['TOTAL_DELAY'] = self.df[delay_columns].fillna(0).sum(axis=1)
            else:
                print("Warning: No delay columns found in the data")
                self.df['TOTAL_DELAY'] = 0
            
            # Load and merge airport coordinates if needed
            if 'ORIGIN_LATITUDE' not in self.df.columns or 'ORIGIN_LONGITUDE' not in self.df.columns:
                print("Loading airport coordinates...")
                try:
                    airports_df = pd.read_csv('airports.csv')
                    print("\nAirport data columns:", airports_df.columns.tolist())
                    
                    # Create a clean airports dataframe
                    airports_clean = pd.DataFrame({
                        'ORIGIN_AIRPORT': airports_df['IATA'],
                        'ORIGIN_LATITUDE': airports_df['LATITUDE'],
                        'ORIGIN_LONGITUDE': airports_df['LONGITUDE']
                    })
                    
                    # Merge with main dataframe
                    self.df = pd.merge(
                        self.df,
                        airports_clean,
                        on='ORIGIN_AIRPORT',
                        how='left'
                    )
                    
                except Exception as e:
                    print(f"Warning: Could not load airport coordinates: {str(e)}")
                    print("Map visualization will not be available.")
            
            print(f"Loaded {len(self.df):,} flights for analysis")
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
        
    def analyze_airline_delays(self):
        """Analyze and visualize delays by airline."""
        plt.figure(figsize=(12, 6))
        
        try:
            # Filter out cancelled flights if 'CANCELLED' column exists
            if 'CANCELLED' in self.df.columns:
                valid_flights = self.df[self.df['CANCELLED'] != 1]
            else:
                valid_flights = self.df
            
            # Group by airline and calculate statistics
            airline_delays = valid_flights.groupby('OP_CARRIER')['TOTAL_DELAY'].agg({
                'mean': 'mean',
                'count': 'size'
            }).reset_index()
            
            # Only show airlines with significant number of flights
            min_flights = len(self.df) * 0.01  # At least 1% of total flights
            airline_delays = airline_delays[airline_delays['count'] >= min_flights]
            
            # Create the plot
            plt.bar(airline_delays['OP_CARRIER'], airline_delays['mean'])
            plt.title('Average Delay by Airline')
            plt.xlabel('Airline')
            plt.ylabel('Average Delay (minutes)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            return airline_delays[['OP_CARRIER', 'mean']].set_index('OP_CARRIER')['mean']
        except Exception as e:
            print(f"Warning: Could not analyze airline delays: {str(e)}")
            return pd.Series()
    
    def analyze_seasonal_trends(self):
        """Analyze seasonal patterns in delays."""
        self.df['Month'] = self.df['FL_DATE'].dt.month
        monthly_delays = self.df.groupby('Month')['TOTAL_DELAY'].mean()
        
        plt.figure(figsize=(10, 6))
        monthly_delays.plot(kind='line', marker='o')
        plt.title('Average Delay by Month')
        plt.xlabel('Month')
        plt.ylabel('Average Delay (minutes)')
        plt.grid(True)
        plt.tight_layout()
        return monthly_delays
    
    def analyze_airport_delays(self):
        """Analyze delays by airport."""
        airport_delays = self.df.groupby('ORIGIN_AIRPORT')['DEP_DELAY'].mean()
        
        plt.figure(figsize=(15, 6))
        airport_delays.nlargest(20).plot(kind='bar')
        plt.title('Top 20 Airports with Longest Average Departure Delays')
        plt.xlabel('Airport')
        plt.ylabel('Average Delay (minutes)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return airport_delays
    
    def visualize_delay_map(self):
        """Create a map visualization of delays across airports."""
        try:
            # Check if we have the required coordinate columns
            if 'ORIGIN_LATITUDE' not in self.df.columns or 'ORIGIN_LONGITUDE' not in self.df.columns:
                print("Warning: Airport coordinate data is not available. Map cannot be created.")
                return
            
            # Load US map data
            self.map_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
            self.map_data = self.map_data[self.map_data.continent == 'North America']
            
            # Create the map
            fig, ax = plt.subplots(figsize=(15, 10))
            self.map_data.plot(ax=ax, alpha=0.5, color='lightgrey')
            
            # Calculate average delays by airport
            airport_delays = self.df.groupby('ORIGIN_AIRPORT').agg({
                'ORIGIN_LONGITUDE': 'first',
                'ORIGIN_LATITUDE': 'first',
                'DEP_DELAY': 'mean'
            }).dropna()
            
            if not airport_delays.empty:
                scatter = ax.scatter(
                    airport_delays['ORIGIN_LONGITUDE'],
                    airport_delays['ORIGIN_LATITUDE'],
                    c=airport_delays['DEP_DELAY'],
                    cmap='YlOrRd',
                    s=100,
                    alpha=0.6
                )
                plt.colorbar(scatter, label='Average Delay (minutes)')
                plt.title('Flight Delays Across US Airports')
            else:
                plt.title('No Airport Delay Data Available')
            
            plt.tight_layout()
            
        except Exception as e:
            print(f"Warning: Could not create map visualization: {str(e)}")

def main():
    try:
        # You can specify your data file path here
        data_file = '2015_flights.csv'  # Updated filename
        
        if not os.path.exists(data_file):
            print(f"Error: Could not find the data file '{data_file}'")
            print("\nPlease download the 2015 Flight Delays dataset from Kaggle:")
            print("https://www.kaggle.com/datasets/usdot/flight-delays")
            print("\nDownload steps:")
            print("1. Visit the link above")
            print("2. Click 'Download' (requires Kaggle account)")
            print("3. Extract the ZIP file")
            print("4. Rename 'flights.csv' to '2015_flights.csv'")
            print("5. Place it in the same directory as this script")
            return
            
        analyzer = FlightDelayAnalyzer(data_file)
        analyzer.load_data()
        
        # Generate all analyses
        airline_delays = analyzer.analyze_airline_delays()
        seasonal_trends = analyzer.analyze_seasonal_trends()
        airport_delays = analyzer.analyze_airport_delays()
        analyzer.visualize_delay_map()
        
        plt.show()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please make sure you have the correct data file format and all required libraries installed.")

if __name__ == "__main__":
    main() 