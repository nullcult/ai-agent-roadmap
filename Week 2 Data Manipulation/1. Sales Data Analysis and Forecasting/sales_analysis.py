import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def load_and_clean_data(file_path):
    """Load and clean the sales data"""
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Handle missing values
    df['quantity'].fillna(df['quantity'].mean(), inplace=True)
    df['price'].fillna(df['price'].mean(), inplace=True)
    
    # Calculate total sale amount
    df['total_amount'] = df['quantity'] * df['price']
    
    return df

def analyze_sales(df):
    """Perform basic sales analysis"""
    # Monthly sales
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum()
    
    # Sales by product
    product_sales = df.groupby('product')['total_amount'].sum().sort_values(ascending=False)
    
    # Sales by region
    region_sales = df.groupby('region')['total_amount'].sum()
    
    return monthly_sales, product_sales, region_sales

def create_visualizations(monthly_sales, product_sales, region_sales):
    """Create various sales visualizations"""
    # Set style
    plt.style.use('seaborn')
    
    # Create figure with subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))
    
    # Monthly sales trend
    monthly_sales.plot(kind='line', ax=ax1)
    ax1.set_title('Monthly Sales Trend')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Sales')
    
    # Top products bar chart
    product_sales.head(10).plot(kind='bar', ax=ax2)
    ax2.set_title('Top 10 Products by Sales')
    ax2.set_xlabel('Product')
    ax2.set_ylabel('Total Sales')
    plt.xticks(rotation=45)
    
    # Regional sales pie chart
    region_sales.plot(kind='pie', ax=ax3, autopct='%1.1f%%')
    ax3.set_title('Sales Distribution by Region')
    
    plt.tight_layout()
    plt.savefig('sales_analysis.png')
    plt.close()

def forecast_sales(monthly_sales, periods=6):
    """Forecast future sales using Holt-Winters method"""
    # Convert to series if not already
    if isinstance(monthly_sales.index, pd.PeriodIndex):
        monthly_sales = monthly_sales.to_timestamp()
    
    # Fit the model
    model = ExponentialSmoothing(
        monthly_sales,
        seasonal_periods=12,
        trend='add',
        seasonal='add'
    ).fit()
    
    # Make forecast
    forecast = model.forecast(periods)
    return forecast

def main():
    # Load and clean data
    df = load_and_clean_data('sales_data.csv')
    
    # Perform analysis
    monthly_sales, product_sales, region_sales = analyze_sales(df)
    
    # Create visualizations
    create_visualizations(monthly_sales, product_sales, region_sales)
    
    # Generate forecast
    forecast = forecast_sales(monthly_sales)
    print("\nSales Forecast for Next 6 Months:")
    print(forecast)

if __name__ == "__main__":
    main() 