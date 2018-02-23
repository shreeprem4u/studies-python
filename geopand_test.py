import geopandas as gpd

# Set filepath (fix path relative to yours)
fp = "/home/researcher/Documents/Premkumar/shapefiles_AB3_Final/floor1/floor1rooms.shp"

# Read file using gpd.read_file()
data = gpd.read_file(fp)
#print(data)# print all data-values in data
#print(data.head())#print first 5 data-values

data.plot()
#print(data.crs)#print crs type of data

selection = data[0:50]
out = r"/home/researcher/Documents/Premkumar/output.shp"
selection.to_file(out)
#print(selection)

#for index, row in selection.iterrows():
#	poly_area = row['geometry'].area
#	print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

# Empty column for area
#selection['area'] = None
# Iterate rows one at the time
for index, row in selection.iterrows():
    # Update the value in 'area' column with area information at index
    selection.loc[index, 'area'] = row['geometry'].area
#print(selection['area'].head(2))
print(selection)


