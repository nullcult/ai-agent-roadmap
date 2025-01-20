import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import geopandas as gpd
from typing import Optional, Tuple

class CrimeVisualizer:
    def __init__(self):
        """Initialize the visualizer with default style settings."""
        plt.style.use('fivethirtyeight')
        self.color_palette = sns.color_palette("husl", 8)
        
    def plot_crime_distribution(self, stats: pd.DataFrame, 
                              title: str = "Crime Type Distribution",
                              figsize: Tuple[int, int] = (12, 6)) -> None:
        """
        Create a bar plot of crime type distribution.
        
        Args:
            stats (pd.DataFrame): Crime statistics with crime types and counts
            title (str): Plot title
            figsize (tuple): Figure size
        """
        plt.figure(figsize=figsize)
        # Rename columns for clarity
        stats.columns = ['Crime Type', 'Count']
        sns.barplot(data=stats, x='Crime Type', y='Count', palette=self.color_palette)
        plt.title(title)
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Crimes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def plot_temporal_trends(self, monthly_stats: pd.DataFrame, 
                           daily_stats: pd.DataFrame,
                           figsize: Tuple[int, int] = (15, 6)) -> None:
        """
        Create plots for temporal trends in crime data.
        
        Args:
            monthly_stats (pd.DataFrame): Monthly crime statistics
            daily_stats (pd.DataFrame): Daily crime statistics
            figsize (tuple): Figure size
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        
        # Monthly trend
        monthly_stats.plot(kind='line', ax=ax1)
        ax1.set_title("Monthly Crime Trend")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Number of Crimes")
        
        # Daily distribution
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_stats.plot(kind='bar', ax=ax2)
        ax2.set_title("Crime Distribution by Day of Week")
        ax2.set_xlabel("Day of Week")
        ax2.set_ylabel("Number of Crimes")
        ax2.set_xticklabels(days, rotation=45)
        
        plt.tight_layout()
        plt.show()
        
    def create_heatmap(self, df: pd.DataFrame, 
                      center: Tuple[float, float],
                      zoom: int = 11) -> folium.Map:
        """
        Create an interactive crime heatmap using Folium.
        
        Args:
            df (pd.DataFrame): Crime data with latitude and longitude
            center (tuple): Map center coordinates (lat, lon)
            zoom (int): Initial zoom level
            
        Returns:
            folium.Map: Interactive heatmap
        """
        # Create base map
        m = folium.Map(location=center, zoom_start=zoom, tiles='CartoDB positron')
        
        # Add heatmap layer
        if 'latitude' in df.columns and 'longitude' in df.columns:
            locations = df[['latitude', 'longitude']].values.tolist()
            HeatMap(locations).add_to(m)
            
        return m
    
    def plot_crime_density(self, gdf: gpd.GeoDataFrame,
                          region_gdf: Optional[gpd.GeoDataFrame] = None,
                          figsize: Tuple[int, int] = (15, 10)) -> None:
        """
        Create a spatial density plot of crimes.
        
        Args:
            gdf (gpd.GeoDataFrame): Crime data as GeoDataFrame
            region_gdf (gpd.GeoDataFrame, optional): Regional boundaries
            figsize (tuple): Figure size
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        if region_gdf is not None:
            region_gdf.plot(ax=ax, alpha=0.4, edgecolor='black')
            
        gdf.plot(ax=ax, alpha=0.5, markersize=5)
        plt.title("Spatial Distribution of Crimes")
        plt.axis('equal')
        plt.show()
        
    def save_visualization(self, fig: plt.Figure, 
                         filename: str,
                         dpi: int = 300) -> None:
        """
        Save the visualization to a file.
        
        Args:
            fig (plt.Figure): Figure to save
            filename (str): Output filename
            dpi (int): Resolution of the output image
        """
        fig.savefig(filename, dpi=dpi, bbox_inches='tight') 