# Crime Data Analysis & Heatmap

This project analyzes crime rates in different regions and visualizes trends over time using public crime datasets.

## Features
- Load and process public crime datasets
- Analyze crime types, frequency, and regional distribution
- Generate crime heatmaps based on locations
- Identify seasonal trends in crimes

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the analysis:
```bash
python main.py
```

## Project Structure
- `main.py`: Main script to run the analysis
- `data_loader.py`: Module for loading and preprocessing crime data
- `visualizer.py`: Module for creating visualizations and heatmaps
- `data/`: Directory for storing crime datasets

## Data Source
This project uses the FBI's Uniform Crime Reporting (UCR) Program data. The data needs to be downloaded separately due to size constraints. 