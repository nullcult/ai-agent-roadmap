import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_sales_data(num_records=1000):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate dates
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=x) for x in range(num_records)]
    
    # Create product list
    products = [f'Product_{i}' for i in range(1, 21)]
    
    # Create regions
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Generate random data
    data = {
        'date': dates,
        'product': np.random.choice(products, num_records),
        'region': np.random.choice(regions, num_records),
        'quantity': np.random.randint(1, 100, num_records),
        'price': np.random.uniform(10, 1000, num_records).round(2)
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add some missing values
    mask = np.random.random(num_records) < 0.05
    df.loc[mask, 'quantity'] = np.nan
    
    # Save to CSV
    df.to_csv('sales_data.csv', index=False)
    print("Mock sales data generated and saved to 'sales_data.csv'")

if __name__ == "__main__":
    generate_mock_sales_data() 