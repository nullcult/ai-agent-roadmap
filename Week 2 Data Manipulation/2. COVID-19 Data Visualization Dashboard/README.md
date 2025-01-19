# COVID-19 Data Visualization Dashboard

This project provides a Python-based dashboard to visualize COVID-19 data from Johns Hopkins University. It includes time-series analysis and world map visualization of confirmed cases, deaths, and recoveries.

## Features

- Loads COVID-19 data directly from Johns Hopkins University GitHub repository
- Processes and cleans the data for analysis
- Generates time-series plots for specific countries
- Creates interactive world map visualizations using Folium
- Tracks confirmed cases, deaths, and recoveries

## Requirements

- Python 3.6+
- Required Python packages:
  - pandas
  - matplotlib
  - seaborn
  - folium

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/covid-dashboard.git
   cd covid-dashboard
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the dashboard:
```bash
python covid_dashboard.py
```

This will:
1. Generate a line chart showing COVID-19 trends for the United States
2. Create an interactive world map saved as `covid_world_map.html`

To visualize data for a different country, modify the `plot_country_trends()` function call in the `main()` function.

## Data Sources

The data is sourced from the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) COVID-19 dataset:
https://github.com/CSSEGISandData/COVID-19

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Screenshots

![Time Series Example](screenshots/time_series.png)
![World Map Example](screenshots/world_map.png)

## Troubleshooting

If the world map is not being created:
1. Ensure you have the required packages installed:
   ```bash
   pip install folium
   ```
2. Check if the data is being loaded correctly
3. Verify that the `processed_data` DataFrame contains valid latitude and longitude values
4. If the issue persists, add print statements to debug the `create_world_map()` function