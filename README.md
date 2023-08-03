# BusStands-On-CycleRoutes-in-Singapore

Provide a list in CSV of bus stand names, latitude and longitude. Then provide a list in CSV of routes line strings, name, description
See Example files in the repo.

## In this code:

- We first define the points (locations) and the cycling route (line string).
- We then create GeoDataFrames for both the points and the line string.
- We use the buffer method to create a buffer around each point. The buffer size can be adjusted according to the required precision. Here, I've used a buffer of 0.001, but this might need to be fine-tuned.
- We then use the intersects method to find points that intersect with the line string (i.e., are within the cycling route).
- Finally, we print the locations that are within the cycling route.

Please note that this code assumes that the coordinates are in a geographic coordinate system (latitude/longitude). If they are in a projected coordinate system (e.g., UTM), the buffer size will need to be adjusted accordingly. Also, you may need to adjust the buffer size based on the granularity of your coordinates and the precision you require.

One more thing to note is that this script checks whether each location falls within a certain distance of the cycling route, not whether it falls exactly on the route. If you need to check whether each location falls exactly on the route, you can remove the buffer method, but this may result in no matches due to the precision of the coordinates.

## Summary of how this script works:  
The script reads location and cycle route data from two CSV files, identifies the locations that fall within the cycle routes, and writes this information to an output CSV file. The script uses the `pandas`, `geopandas`, and `shapely` libraries for data manipulation and geospatial analysis.

## step-by-step explanation of the script:

1. **Import necessary libraries:**
The script imports the required Python libraries. `pandas` is used for data manipulation, `geopandas` for geospatial operations, and `shapely` for creating and operating on shape geometries like points and lines.

2. **Load location data:**
The script reads location data from a CSV file using `pandas.read_csv`. It expects the CSV file to have columns "Location", "Lat", and "Long".

3. **Create Point geometries:**
The script converts the latitude and longitude in the location data to `shapely.Point` objects. This is necessary for the subsequent geospatial analysis.

4. **Create GeoDataFrame for locations:**
A GeoDataFrame is a data structure from the `geopandas` library that is similar to a `pandas` DataFrame but with additional features for geospatial data. The script creates a GeoDataFrame for the location data, with the `shapely.Point` objects as the geometry.

5. **Load cycle route data:**
The script reads cycle route data from a CSV file. It expects the CSV file to have a "WKT" column with the Well-Known Text (WKT) representation of the cycle routes.

6. **Create LineString geometries:**
The script converts the WKT in the cycle route data to `shapely.LineString` objects using the `shapely.wkt.loads` function.

7. **Create GeoDataFrame for cycle routes:**
The script creates a GeoDataFrame for the cycle route data, with the `shapely.LineString` objects as the geometry.

8. **Initialize output DataFrame:**
The script initializes a `pandas.DataFrame` to store the output data. The output data consists of the route name, location name, latitude, and longitude.

9. **Identify locations within cycle routes:**
For each cycle route, the script finds the locations that are within the route by creating a buffer around each location and checking if it intersects with the route. The size of the buffer can be adjusted as needed. The script adds the locations that are within each route to the output DataFrame, along with the route name.

10. **Write output to CSV file:**
Finally, the script writes the output DataFrame to a CSV file. Each row in the file represents a location that is within a route, along with the name of the route.

The script is designed to be flexible and easily adaptable to different data structures and requirements. It demonstrates the use of Python for geospatial analysis using `pandas`, `geopandas`, and `shapely`.

I hope this gives you a clear understanding of the script. Let me know if you have any further questions.
