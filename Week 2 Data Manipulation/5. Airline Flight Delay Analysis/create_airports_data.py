import pandas as pd

# Common US airports data
airports_data = {
    'IATA': [
        'ATL', 'LAX', 'ORD', 'DFW', 'DEN', 'JFK', 'SFO', 'SEA', 'LAS', 'MCO',
        'EWR', 'CLT', 'PHX', 'IAH', 'MIA', 'BOS', 'MSP', 'DTW', 'FLL', 'PHL'
    ],
    'LATITUDE': [
        33.6367, 33.9425, 41.9786, 32.8968, 39.8561, 40.6398, 37.6188, 47.4499, 36.0840, 28.4294,
        40.6925, 35.2140, 33.4342, 29.9844, 25.7932, 42.3656, 44.8820, 42.2124, 26.0725, 39.8721
    ],
    'LONGITUDE': [
        -84.4281, -118.4081, -87.9048, -97.0380, -104.6737, -73.7789, -122.3756, -122.3117, -115.1537, -81.3089,
        -74.1687, -80.9431, -112.0080, -95.3414, -80.2906, -71.0096, -93.2218, -83.3534, -80.1527, -75.2405
    ],
    'AIRPORT_NAME': [
        'Hartsfield-Jackson Atlanta International', 'Los Angeles International', "Chicago O'Hare International",
        'Dallas/Fort Worth International', 'Denver International', 'John F. Kennedy International',
        'San Francisco International', 'Seattle-Tacoma International', 'McCarran International',
        'Orlando International', 'Newark Liberty International', 'Charlotte Douglas International',
        'Phoenix Sky Harbor International', 'George Bush Intercontinental', 'Miami International',
        'Logan International', 'Minneapolis-Saint Paul International', 'Detroit Metropolitan',
        'Fort Lauderdale-Hollywood International', 'Philadelphia International'
    ]
}

# Create DataFrame and save to CSV
airports_df = pd.DataFrame(airports_data)
airports_df.to_csv('airports.csv', index=False)
print("Created airports.csv with data for 20 major US airports") 