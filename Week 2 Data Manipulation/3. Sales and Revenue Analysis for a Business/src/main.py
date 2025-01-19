import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from data_processor import DataProcessor
from analysis import SalesAnalyzer
from visualizer import DataVisualizer

def main():
    # Create output directory if it doesn't exist
    Path("output").mkdir(exist_ok=True)
    
    # Initialize components
    processor = DataProcessor()
    analyzer = SalesAnalyzer()
    visualizer = DataVisualizer()
    
    try:
        # Load and process data
        df = processor.load_data("data/sample_sales_data.csv")
        cleaned_df = processor.clean_data(df)
        
        # Perform analysis
        monthly_sales = analyzer.calculate_monthly_sales(cleaned_df)
        top_products = analyzer.identify_top_products(cleaned_df)
        regional_performance = analyzer.analyze_regional_performance(cleaned_df)
        
        # Create visualizations
        visualizer.plot_monthly_trends(monthly_sales)
        visualizer.plot_top_products(top_products)
        visualizer.create_sales_heatmap(cleaned_df)
        
        print("Analysis completed successfully!")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
