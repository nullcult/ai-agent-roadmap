import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def plot_monthly_trends(self, monthly_sales):
        """
        Plot monthly sales trends
        """
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_sales['date'], monthly_sales['revenue'], marker='o')
        plt.title('Monthly Sales Trends')
        plt.xlabel('Month')
        plt.ylabel('Revenue ($)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(monthly_sales['date'], monthly_sales['date'].dt.strftime('%Y-%m'), rotation=45)
        plt.tight_layout()
        plt.savefig('output/monthly_trends.png')
        plt.close()
    
    def plot_top_products(self, top_products):
        """
        Create bar plot of top products
        """
        plt.figure(figsize=(12, 6))
        sns.barplot(data=top_products.reset_index(), x='product_name', y='revenue')
        plt.title('Top Products by Revenue')
        plt.xlabel('Product')
        plt.ylabel('Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('output/top_products.png')
        plt.close()
    
    def create_sales_heatmap(self, df):
        """
        Create heatmap for sales patterns
        """
        pivot_table = df.pivot_table(
            values='quantity',
            index=df['date'].dt.dayofweek,
            columns=df['date'].dt.hour,
            aggfunc='sum'
        )
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_table, cmap='YlOrRd', annot=True, fmt='.0f')
        plt.title('Sales Heatmap (Day of Week vs Hour)')
        plt.xlabel('Hour of Day')
        plt.ylabel('Day of Week')
        plt.tight_layout()
        plt.savefig('output/sales_heatmap.png')
        plt.close()
