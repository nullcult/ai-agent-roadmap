# Flight Delay Analysis Tool

A Python-based analysis tool for exploring and visualizing airline flight delay patterns across the United States using real flight data from 2015.

## Data Requirements

1. **Main Flight Data** (required):
   - Download from [2015 Flight Delays Dataset](https://www.kaggle.com/datasets/usdot/flight-delays)
   - Extract `flights.csv` and rename to `2015_flights.csv`

2. **Airport Data** (required for map visualization):
   - From the same dataset, extract `airports.csv`
   - Contains airport coordinates needed for the map

The files should contain these columns:

**2015_flights.csv:**
- `FL_DATE`: Flight date
- `OP_CARRIER`: Two letter airline code
- `ORIGIN`: Three letter origin airport code
- `DEP_DELAY`: Departure delay in minutes
- `ARR_DELAY`: Arrival delay in minutes
- `CANCELLED`: Flight cancellation flag (0/1)

**airports.csv:**
- `IATA`: Three letter airport code
- `LATITUDE`: Airport latitude
- `LONGITUDE`: Airport longitude
- `AIRPORT_NAME`: Full airport name

## Quick Start

1. **Download the Data**:
   - Visit [2015 Flight Delays Dataset](https://www.kaggle.com/datasets/usdot/flight-delays)
   - Download and extract both files:
     - Rename `flights.csv` to `2015_flights.csv`
     - Keep `airports.csv` as is
   - Place both files in the project directory

2. **Install Requirements**:
   ```