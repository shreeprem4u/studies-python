
import matplotlib.pyplot as plt
import shapefile
import matplotlib
from mpl_toolkits.basemap import Basemap
import numpy as np


sf = shapefile.Reader("/home/researcher/Documents/Premkumar/shapefiles_AB3_Final/floor1/floor1rooms.dbf")
listx=[]
listy=[]

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
#points = []dict(arrowstyle="fancy", color='g'
#points[0] = 76000
#points[1] = 23500
'''x=75000
y=23000
x2=75000
y2=25000'''
#plt.annotate("P1", xy=(x,y), xytext=(x2,y2), xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="fancy", color='g'), color = 'r')
#plt.text.Annotation(P1, xy, xytext=None, xycoords='data', textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)
print 'number of shapes imported:',len(sf.shapes())

shape_ex = sf.shape(5)
'''
x_lon = np.zeros((len(shape_ex.points),1))
y_lat = np.zeros((len(shape_ex.points),1))
for ip in range(len(shape_ex.points)):
    x_lon[ip] = shape_ex.points[ip][0]
    y_lat[ip] = shape_ex.points[ip][1]

plt.plot(x_lon,y_lat)# use bbox (bounding box) to set plot limits
plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
'''
plt.show()




