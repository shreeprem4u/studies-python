# Import necessary modules first
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import fiona
import csv
import numpy as np

# Create an empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()
print(newdata)

# Create a new column called 'geometry' to the GeoDataFrame
newdata['geometry'] = None

data = pd.DataFrame([[(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)],[(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)]], dtype='float')

print(data)



'''
coords = np.array([[(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)],[(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)]])
print(coords)
for i in coords:
	poly = Polygon(coords)
	print(poly)

file = open("/home/researcher/Documents/Premkumar/python/staffroomCords.csv", "r")

myreader = csv.reader(file)
for row in myreader:
#	cords = row
#	p1 = Polygon(cords)
	print(row)

#Coordinates of P1
coordinates = [(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)]
# Create a Shapely polygon from the coordinate-tuple list
poly = Polygon(coordinates)
# Insert the polygon into 'geometry' -column at index 0
newdata.loc[0, 'geometry'] = poly
#print(newdata)

#newdata.plot()

# Add a new column and insert data
newdata.loc[0, 'Location'] = 'P1'
print(newdata)
print(newdata.crs)

# Import specific function 'from_epsg' from fiona module
from fiona.crs import from_epsg

# Set the GeoDataFrame's coordinate system to WGS84
newdata.crs = from_epsg(4326)
print(newdata.crs)

# Determine the output path for the Shapefile
outfp = r"/home/researcher/Documents/Premkumar/python/staffroom.shp"

# Write the data into that Shapefile
newdata.to_file(outfp)
'''




