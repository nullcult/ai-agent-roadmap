import pandas as pd

class SalesAnalyzer:
    def calculate_monthly_sales(self, df):
        """
        Calculate monthly sales trends
        """
        monthly_sales = df.groupby(df['date'].dt.strftime('%Y-%m')).agg({
            'revenue': 'sum',
            'quantity': 'sum'
        }).reset_index()
        monthly_sales['date'] = pd.to_datetime(monthly_sales['date'] + '-01')
        return monthly_sales
    
    def identify_top_products(self, df, top_n=10):
        """
        Identify best-performing products
        """
        top_products = df.groupby('product_name').agg({
            'revenue': 'sum',
            'quantity': 'sum'
        }).sort_values('revenue', ascending=False).head(top_n)
        return top_products
    
    def analyze_regional_performance(self, df):
        """
        Analyze sales performance by region
        """
        regional_performance = df.groupby('region').agg({
            'revenue': 'sum',
            'quantity': 'sum'
        }).sort_values('revenue', ascending=False)
        return regional_performance
