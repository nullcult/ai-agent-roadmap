import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from datetime import datetime
import os
import requests
import numpy as np

# Load COVID-19 data from Johns Hopkins University GitHub repository
def load_data():
    try:
        # Direct URLs to time series data
        urls = {
            'confirmed': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv',
            'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
        }
        
        data = {}
        for key, url in urls.items():
            print(f"Loading {key} data...")
            data[key] = pd.read_csv(url)
            print(f"Successfully loaded {key} data")
        
        return data['confirmed'], data['deaths']
    
    except Exception as e:
        raise Exception(f"Failed to load data: {str(e)}")

# Process and clean the data
def process_data(confirmed, deaths):
    try:
        # Get the latest date from the columns (last column)
        date_cols = confirmed.columns[11:]  # Skip the first 11 columns which are metadata
        latest_date = date_cols[-1]
        
        # Extract relevant columns
        processed_data = pd.DataFrame({
            'Province/State': confirmed['Province_State'],
            'Lat': confirmed['Lat'],
            'Long': confirmed['Long_'],
            'Confirmed': confirmed[latest_date],
            'Deaths': deaths[latest_date]
        })
        
        # Group by state
        state_data = processed_data.groupby('Province/State').agg({
            'Lat': 'mean',
            'Long': 'mean',
            'Confirmed': 'sum',
            'Deaths': 'sum'
        }).reset_index()
        
        print("\nProcessed US data shape:", state_data.shape)
        print("Sample of processed US data:")
        print(state_data.head())
        
        return state_data
    
    except Exception as e:
        raise Exception(f"Failed to process data: {str(e)}")

# Plot time series for a specific country
def plot_us_trends(data):
    try:
        # Create figure with subplot
        plt.figure(figsize=(15, 10))
        
        # Sort states by confirmed cases
        states_data = data.sort_values('Confirmed', ascending=True)
        
        # Create horizontal bar chart
        plt.barh(states_data['Province/State'], states_data['Confirmed'], 
                label='Confirmed', alpha=0.8)
        plt.barh(states_data['Province/State'], states_data['Deaths'], 
                label='Deaths', alpha=0.8)
        
        plt.title('COVID-19 Cases by US State')
        plt.xlabel('Number of Cases')
        plt.ylabel('State')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error creating plot: {str(e)}")

# Create world map visualization
def create_us_map(data):
    try:
        # Create base map centered on US
        us_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
        
        # Add markers for each state
        for idx, row in data.iterrows():
            folium.CircleMarker(
                location=[row['Lat'], row['Long']],
                radius=min(int(np.log(row['Confirmed'] + 1) * 2), 30),  # Log scale for better visualization
                color='red',
                fill=True,
                fill_color='red',
                popup=f"""
                    <b>{row['Province/State']}</b><br>
                    Confirmed: {int(row['Confirmed']):,}<br>
                    Deaths: {int(row['Deaths']):,}<br>
                """
            ).add_to(us_map)
        
        return us_map
    
    except Exception as e:
        print(f"Error creating US map: {str(e)}")
        return None

# Main function to run the dashboard
def main():
    try:
        print("Starting US COVID-19 Dashboard...")
        
        # Load and process data
        print("\nLoading US data...")
        confirmed, deaths = load_data()
        
        print("\nProcessing US data...")
        processed_data = process_data(confirmed, deaths)
        
        # Generate visualizations
        print("\nGenerating US trends plot...")
        plot_us_trends(processed_data)
        
        # Create and save US map
        print("\nCreating US map...")
        us_map = create_us_map(processed_data)
        if us_map:
            us_map.save('us_covid_map.html')
            print("US map successfully saved as us_covid_map.html")
        else:
            print("Failed to create US map")
            
    except Exception as e:
        print(f"\nError running dashboard: {str(e)}")
        raise

if __name__ == "__main__":
    main() 