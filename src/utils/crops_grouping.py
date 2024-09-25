import pandas as pd

# Load the dataset to inspect its contents
file_path = '../../data/crops.csv'
data = pd.read_csv(file_path)

# Define regions and their associated counties
regions = {
    'San Francisco': ['Del Norte', 'Humboldt', 'Mendocino', 'Sonoma', 'Marin', 'San Francisco', 'San Mateo',
                       'Santa Cruz', 'Monterey', 'San Luis Obispo', 'Santa Barbara', 'Ventura', 'Los Angeles',
                       'Orange', 'San Diego'],
    'Riverside': ['Riverside', 'San Bernardino'],
    'Fresno': ['Fresno', 'Sacramento', 'San Joaquin', 'Stanislaus', 'Merced', 'Madera', 'Kings', 'Tulare',
                       'Kern', 'Yolo', 'Colusa', 'Sutter', 'Butte', 'Glenn', 'Tehama'],
    'South Lake Tahoe': ['Alpine', 'Amador', 'Calaveras', 'El Dorado', 'Inyo', 'Lassen', 'Mariposa', 'Mono',
                        'Nevada', 'Plumas', 'Sierra', 'Tuolumne'],
    'Palm Springs': ['Imperial', 'Inyo', 'San Bernardino', 'Riverside'],
    'Eureka': ['Del Norte', 'Humboldt', 'Mendocino', 'Trinity', 'Siskiyou', 'Shasta', 'Tehama', 'Lassen',
                            'Modoc', 'Plumas', 'Butte'],
    'Los Angeles': ['Los Angeles', 'Orange', 'San Diego', 'Ventura', 'San Bernardino', 'Riverside', 'Imperial']
}

# Create a new column in the dataset for the region
def assign_region(county):
    for region, counties in regions.items():
        if county in counties:
            return region
    return 'Unknown Region'

# Apply the function to assign regions
data['Region'] = data['County'].apply(assign_region)

# Filter data for the years 1980 to 2022
data_filtered = data[(data['Year'] >= 1980) & (data['Year'] <= 2022)]

# Group by 'Region' and 'Year', and compute the mean of the relevant numerical columns
grouped_data = data_filtered.groupby(['Region', 'Year', 'Crop Name']).agg({
    'Harvested Acres': 'mean',
    'Yield': 'mean',
    'Production': 'mean',
    'Price P/U': 'mean',
    'Value': 'mean'
}).reset_index()

# Output the grouped data to a new CSV file
output_file_path = '../../data/grouped_counties_by_region.csv'
grouped_data.to_csv(output_file_path)
