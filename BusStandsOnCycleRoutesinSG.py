# Ritesh Sinha 
# 03-Aug-2023 

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
from shapely import wkt

# Load locations data
# Locations data format is :  
#  Location	Lat	Long
#  Lcation name, x.xxxxxxx, y.yyyyyyy 
#

locations_df = pd.read_csv('locations.csv')

# Convert lat/lon to shapely Point objects
locations_df['geometry'] = locations_df.apply(lambda row: Point(row['Long'], row['Lat']), axis=1)

# Create a GeoDataFrame from the locations
locations_gdf = gpd.GeoDataFrame(locations_df, geometry='geometry')

# Load routes data
# Route Data format is : 
#   WKT,	name,	description
#   linestring, location1, this is a location. 

routes_df = pd.read_csv('routes.csv')

# Convert WKT to shapely LineString objects
routes_df['geometry'] = routes_df['WKT'].apply(wkt.loads)

# Create a GeoDataFrame from the routes
routes_gdf = gpd.GeoDataFrame(routes_df, geometry='geometry')

# Create a DataFrame to store the output
output_df = pd.DataFrame(columns=['Route Name', 'Location', 'Lat', 'Long'])

# For each route, find the locations that are within the route
for i, route in routes_gdf.iterrows():
    locations_gdf['intersect'] = locations_gdf.geometry.buffer(0.001).intersects(route.geometry)

    # Get locations that are within the route
    intersect_locations = locations_gdf[locations_gdf['intersect'] == True]

    # Add the locations to the output DataFrame
    for j, location in intersect_locations.iterrows():
        output_df = output_df._append({
            'Route Name': route['name'],
            'Location': location['Location'],
            'Lat': location['Lat'],
            'Long': location['Long']
        }, ignore_index=True)

# Write the output DataFrame to a CSV file
# format is  
# Route Name	Location	Lat	Long
#

output_df.to_csv('output.csv', index=False)
