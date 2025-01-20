import pandas as pd
import geopandas as gpd
from pathlib import Path
import requests
from typing import Tuple, Optional

class CrimeDataLoader:
    def __init__(self, data_dir: str = "data"):
        """Initialize the data loader with a data directory."""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
    def load_crime_data(self, file_path: str) -> pd.DataFrame:
        """
        Load crime data from a CSV file.
        
        Args:
            file_path (str): Path to the crime data CSV file
            
        Returns:
            pd.DataFrame: Processed crime data
        """
        print("Reading CSV file...")
        # Read only necessary columns to save memory
        df = pd.read_csv(file_path, usecols=['Date', 'Primary Type', 'Latitude', 'Longitude'])
        
        # Clean the data by removing rows where Date is not in the expected format
        print("Cleaning data...")
        date_pattern = r'\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}\s+[AaPp][Mm]'
        mask = df['Date'].str.match(date_pattern, na=False)
        invalid_dates = df[~mask]
        if len(invalid_dates) > 0:
            print(f"\nFound {len(invalid_dates)} rows with invalid date format. Examples:")
            print(invalid_dates['Date'].head())
            print("\nRemoving invalid dates...")
            df = df[mask]
        
        print(f"Loaded {len(df)} valid records.")
        return self._preprocess_crime_data(df)
    
    def _preprocess_crime_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the crime data.
        
        Args:
            df (pd.DataFrame): Raw crime data
            
        Returns:
            pd.DataFrame: Preprocessed crime data
        """
        print("Preprocessing data...")
        
        # Convert date columns to datetime
        if 'Date' in df.columns:
            try:
                # Convert dates using the known format
                df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')
                print("Date conversion successful.")
                print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
            except Exception as e:
                print(f"Error converting dates: {e}")
                print("Sample of dates:")
                print(df['Date'].head())
                raise ValueError("Failed to convert dates. Please check the date format.")
        
        # Drop rows with missing coordinates
        if 'Latitude' in df.columns and 'Longitude' in df.columns:
            initial_rows = len(df)
            df = df.dropna(subset=['Latitude', 'Longitude'])
            dropped_rows = initial_rows - len(df)
            if dropped_rows > 0:
                print(f"Dropped {dropped_rows} rows with missing coordinates.")
            
            # Rename columns to match our expected format
            df = df.rename(columns={
                'Primary Type': 'crime_type',
                'Latitude': 'latitude',
                'Longitude': 'longitude'
            })
        
        print("Preprocessing complete.")
        print(f"Final dataset shape: {df.shape}")
        return df
    
    def get_crime_stats(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate basic crime statistics.
        
        Args:
            df (pd.DataFrame): Crime data
            
        Returns:
            pd.DataFrame: Crime statistics
        """
        if 'crime_type' in df.columns:
            # Get top 10 crime types for better visualization
            stats = df['crime_type'].value_counts().head(10).reset_index()
            stats.columns = ['Crime Type', 'Count']
            print(f"Generated statistics for top {len(stats)} crime types.")
            return stats
        return pd.DataFrame()
    
    def get_temporal_stats(self, df: pd.DataFrame, date_column: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Calculate temporal crime statistics.
        
        Args:
            df (pd.DataFrame): Crime data
            date_column (str): Name of the date column
            
        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: Monthly and daily crime counts
        """
        if date_column not in df.columns:
            print(f"Error: {date_column} column not found in the dataset")
            return pd.DataFrame(), pd.DataFrame()
            
        try:
            # Ensure we're working with datetime
            if not pd.api.types.is_datetime64_any_dtype(df[date_column]):
                print(f"Warning: {date_column} is not in datetime format. Attempting conversion...")
                df[date_column] = pd.to_datetime(df[date_column])
            
            # Monthly statistics (all months in the dataset)
            print("Calculating monthly statistics...")
            monthly_stats = df.groupby(df[date_column].dt.to_period('M')).size()
            print(f"Generated monthly statistics for {len(monthly_stats)} months")
            print(f"Time range: {monthly_stats.index.min()} to {monthly_stats.index.max()}")
            
            # Daily statistics by day of week
            print("\nCalculating daily statistics...")
            daily_stats = df.groupby(df[date_column].dt.dayofweek).size()
            # Convert day numbers to names
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            daily_stats.index = day_names
            print("Generated daily statistics for all days of the week")
            
            return monthly_stats, daily_stats
            
        except Exception as e:
            print(f"Error generating temporal statistics: {e}")
            print("Date column sample:")
            print(df[date_column].head())
            return pd.DataFrame(), pd.DataFrame()
    
    def create_geodataframe(self, df: pd.DataFrame) -> Optional[gpd.GeoDataFrame]:
        """
        Convert DataFrame to GeoDataFrame if coordinates are available.
        
        Args:
            df (pd.DataFrame): Crime data with latitude and longitude
            
        Returns:
            gpd.GeoDataFrame or None: GeoDataFrame with crime locations
        """
        if 'latitude' in df.columns and 'longitude' in df.columns:
            return gpd.GeoDataFrame(
                df, 
                geometry=gpd.points_from_xy(df.longitude, df.latitude),
                crs="EPSG:4326"
            )
        return None 