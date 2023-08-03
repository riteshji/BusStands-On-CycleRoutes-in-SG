# BusStands-On-CycleRoutes-in-SG

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
