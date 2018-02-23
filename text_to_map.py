from shapely.geometry import Point, LineString, Polygon
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

file = open("/home/researcher/Documents/Premkumar/python/check_data.csv", "r")

myreader = csv.reader(file)
header = myreader.next()
x = header.index("x")
y = header.index("y")

data = []
plt.figure()
for row in myreader:
	x_value = row[x]
	y_value = row[y]
	data.append([x_value,y_value])
	plt.plot(int(x_value),int(y_value))
	

print data
plt.show()



