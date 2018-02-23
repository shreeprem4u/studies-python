# Import necessary modules first
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import fiona
import csv
import numpy as np
import matplotlib.pyplot as plt

# Create an empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()
print(newdata)

# Create a new column called 'geometry' to the GeoDataFrame
newdata['geometry'] = None
print(newdata)

#Coordinates of P1 to P5
coords = [[(746429.28183,210419.94685), (746429.28183,214282.14268), (754336.88021,214282.14268),(754336.88021,210411.28167), (746429.28183,210419.94685)],[(754473.04737,210418.70897),(754473.04737,214280.90480),(758345.14626,214280.90480),(758345.14626,210418.70897),(754473.04737,210418.70897)],[(758503.59532,210418.70897),(758503.59532,214280.90480),(762365.79115,214280.90480),(762375.69421,210418.70897),(758503.59532,210418.70897)],[(762504.43407,210418.70897),(762514.33714,214280.90480),(766386.43603,214280.90480),(766396.33910,210418.70897),(762504.43407,210418.70897)],[(766530.03049,210418.70897),(766539.93356,214280.90480),(770412.03245,214280.90480),(770421.93552,210418.70897),(766530.03049,210418.70897)]]

l = len(coords)

for i in range(0,l):
	p1 = Polygon(coords[i])
	newdata.loc[i, 'geometry'] = p1
#	print(p1)

print(newdata)


# Import specific function 'from_epsg' from fiona module
from fiona.crs import from_epsg

# Set the GeoDataFrame's coordinate system to WGS84
newdata.crs = from_epsg(4326)
print(newdata.crs)

# Determine the output path for the Shapefile
outfp = r"/home/researcher/Documents/Premkumar/python/staffroom.shp"

# Write the data into that Shapefile
newdata.to_file(outfp)

newdata.plot()
plt.show()


  
