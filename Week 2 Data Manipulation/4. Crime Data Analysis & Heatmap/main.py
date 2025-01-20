import pandas as pd
import numpy as np
from pathlib import Path
from data_loader import CrimeDataLoader
from visualizer import CrimeVisualizer

def main():
    # Initialize the data loader and visualizer
    data_loader = CrimeDataLoader()
    visualizer = CrimeVisualizer()
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # File path for the Chicago Crime Dataset
    chicago_crime_file = data_dir / "Chicago_Crimes_2001_to_2004.csv"
    
    if not chicago_crime_file.exists():
        print(f"Error: Dataset file not found at {chicago_crime_file}")
        print("Please ensure the Chicago Crimes 2001-2004 dataset is in the data directory.")
        return
    
    print("Loading crime data...")
    crime_data = data_loader.load_crime_data(chicago_crime_file)
    
    # Get crime statistics
    print("Calculating crime statistics...")
    crime_stats = data_loader.get_crime_stats(crime_data)
    
    # Get temporal statistics
    print("Analyzing temporal patterns...")
    monthly_stats, daily_stats = data_loader.get_temporal_stats(crime_data, 'Date')
    
    # Create visualizations
    print("Generating crime distribution plot...")
    visualizer.plot_crime_distribution(crime_stats)
    
    print("Generating temporal trends plot...")
    visualizer.plot_temporal_trends(monthly_stats, daily_stats)
    
    print("Generating crime heatmap...")
    # Chicago coordinates
    map_center = (41.8781, -87.6298)
    crime_map = visualizer.create_heatmap(crime_data, map_center)
    crime_map.save(data_dir / "chicago_crime_heatmap_2001_2004.html")
    
    # Create GeoDataFrame for spatial analysis
    gdf = data_loader.create_geodataframe(crime_data)
    if gdf is not None:
        print("Generating spatial density plot...")
        visualizer.plot_crime_density(gdf)
    
    print("\nAnalysis complete! Check the data directory for output files.")

if __name__ == "__main__":
    main() 