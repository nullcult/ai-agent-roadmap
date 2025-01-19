# Sales Data Analysis and Forecasting

This project provides tools for analyzing sales data and generating sales forecasts. It includes functionality for data cleaning, visualization, and time series forecasting using the Holt-Winters method.

## Installation

1. Make sure you have Python 3.7+ installed on your system

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. First, generate mock sales data (if you don't have your own dataset):
```bash
python generate_mock_data.py
```

2. Run the sales analysis:
```bash
python sales_analysis.py
```

This will:
- Generate visualizations saved as 'sales_analysis.png'
- Print sales forecasts for the next 6 months

## Input Data Format

If you're using your own data, ensure your CSV file has the following columns:
- date: Date of sale (YYYY-MM-DD format)
- product: Product name/ID
- region: Sales region
- quantity: Number of units sold
- price: Price per unit

## Output

The script generates:
1. A PNG file ('sales_analysis.png') containing three visualizations:
   - Monthly sales trend (line chart)
   - Top 10 products by sales (bar chart)
   - Regional sales distribution (pie chart)
2. Console output showing sales forecasts for the next 6 months

## Customization

- To modify the number of mock records, edit the `num_records` parameter in `generate_mock_data.py`
- To adjust the forecast period, modify the `periods` parameter in the `forecast_sales()` function call
- To change visualization styles, edit the `create_visualizations()` function in `sales_analysis.py`

## File Structure

- `sales_analysis.py`: Main analysis script
- `generate_mock_data.py`: Mock data generation script
- `sales_data.csv`: Generated/input sales data
- `sales_analysis.png`: Output visualizations

## Contributing

Feel free to submit issues and enhancement requests!
