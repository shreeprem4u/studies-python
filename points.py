# -*- coding: utf-8 -*-
# Import necessary geometric objects from shapely module
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, box

# Create Point geometric object(s) with coordinates
point1 = Point(2.2, 4.2)

point2 = Point(7.2, -25.1)

point3 = Point(9.26, -2.456)

point3D = Point(9.26, -2.456, 0.57)
'''
#point_type = type(point1)

print(point1)

print(point3D)

#print(type(point1))

#print(point_type)

# Get the coordinates
point_coords = point1.coords #point_coords is an object for shapely.coords.CoordinateSequence


# Get x and y coordinates
xy = point_coords.xy

print(xy)

point_dist = point1.distance(point2)

print(point_dist) # output is Euclidean distance between point1 and point2. Ans: 29.7235596792

print("Distance between the points is {0:.2f} decimal degrees".format(point_dist)) #output: Distance between the points is 29.72 decimal degrees


# Create a LineString from our Point objects
line = LineString([point1, point2, point3])

# It is also possible to use coordinate tuples having the same outcome
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

print(line)

print(line2)

print(type(line))

# Get x and y coordinates of the line
lxy = line.xy

print(lxy) # all x's in Row0 and all y's in Row1 

# Extract x coordinates
line_x = lxy[0]

# Extract y coordinates straight from the LineObject by referring to a array at index 1
line_y = line.xy[1]

print(line_x)


print(line_y)

# Get the lenght of the line
l_length = line.length

# Get the centroid of the line
l_centroid = line.centroid

# What type is the centroid?
centroid_type = type(l_centroid)
centroid_type2 = l_centroid.geom_type # geom_type used to get output as text


# Print the outputs
print("Length of our line: {0:.2f}".format(l_length))

print("line of our line: ", l_length)

print("Centroid of our line: ", l_centroid) # it doesn't give the expected output

#see the difference in the below two output for working of geom_type
print("Type of the centroid:", centroid_type) #output: <class 'shapely.geometry.point.Point'>
print("Type of the centroid2:", centroid_type2) # output: Point


# Create a Polygon from the coordinates
poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

# We can also use our previously created Point objects (same outcome)
# --> notice that Polygon object requires x,y coordinates as input
poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])


print(poly2) #output: POLYGON ((2.2 4.2, 7.2 -25.1, 9.26 -2.456, 2.2 4.2)) // Need not to give finishing coords while defining the polygon. it takes first coords valus as last of its own


#Notice that Polygon has double parentheses around the coordinates. This is because Polygon can also have holes inside of it. As the help of Polygon -object tells, a Polygon can be constructed using exterior coordinates and interior coordinates (optional) where the interior coordinates creates a hole inside the Polygon:


#CREATE A POLYGON WITH A HOLE INSIDE

# Let's create a bounding box of the world and make a whole in it
# First we define our exterior
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# Let's create a single big hole where we leave ten decimal degrees at the boundaries of the world
# Notice: there could be multiple holes, thus we need to provide a list of holes
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

# World without a hole
world = Polygon(shell=world_exterior)

# Now we can construct our Polygon with the hole inside
world_has_a_hole = Polygon(shell=world_exterior, holes=hole)

print(world)

print(world_has_a_hole)

#POLYGON ATTRIBUTES AND FUNCTIONS

# Get the centroid of the Polygon
world_centroid = world.centroid 

# Get the area of the Polygon
world_area = world.area

# Get the bounds of the Polygon (i.e. bounding box)
world_bbox = world.bounds

# Get the exterior of the Polygon
world_ext = world.exterior

# Get the length of the exterior
world_ext_length = world.length

#Let’s see what we have now

print("Poly centroid: ", world_centroid) #  NOT WORKING. OUTPUT should be : Poly centroid:  POINT (-0 -0)

print("Poly Area: ", world_area) #Poly Area:  64800.0

print("Poly Bounding Box: ", world_bbox) #Poly Bounding Box:  (-180.0, -90.0, 180.0, 90.0)

print("Poly Exterior: ", world_ext) #NOT WORKING. OUTPUT should be : Poly Exterior:  LINEARRING (-180 90, -180 -90, 180 -90, 180 90, -180 90)

print("Poly Exterior Length: ", world_ext_length) #Poly Exterior Length:  1080.0
'''

# Create a MultiPoint object of our points 1,2 and 3
multi_point = MultiPoint([point1, point2, point3])

# It is also possible to pass coordinate tuples inside
#multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

# We can also create a MultiLineString with two lines
line1 = LineString([point1, point2])

line2 = LineString([point2, point3])

multi_line = MultiLineString([line1, line2])

#print(line2)

#print(multi_line)


# MultiPolygon can be done in a similar manner
# Let's divide our world into western and eastern hemispheres with a hole on the western hemisphere
# --------------------------------------------------------------------------------------------------
# Let's create the exterior of the western part of the world
west_exterior = [(-180, 90), (-180, -90), (0, -90), (0, 90)]

# Let's create a hole --> remember there can be multiple holes, thus we need to have a list of hole(s).
# Here we have just one.
west_hole = [[(-170, 80), (-170, -80), (-10, -80), (-10, 80)]]

# Create the Polygon
west_poly = Polygon(shell=west_exterior, holes=west_hole)

# Let's create the Polygon of our Eastern hemisphere polygon using bounding box
# For bounding box we need to specify the lower-left corner coordinates and upper-right coordinates
min_x, min_y = 0, -90

max_x, max_y = 180, 90

# Create the polygon using box() function
east_poly_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)

# Let's create our MultiPolygon. We can pass multiple Polygon -objects into our MultiPolygon as a list
multi_poly = MultiPolygon([west_poly, east_poly_box]) # Be AWARE of [ ] inside function. it says [0] is west_poly and [1] is east_poly_box


#print("MultiPoint:", multi_point)

#print("MultiLine: ", multi_line)

#print("Bounding box: ", east_poly_box)

#print("MultiPoly: ", multi_poly)

#print(multi_point) # THIS IS WORKING

#print("MultiLine: ") # THIS IS WORKING
#print(multi_line)

#print("Bounding box: ", east_poly_box) # BUT IT GIVES UNEXPECTED OUTPUT

#print("MultiPoly: ", multi_poly)

#Geometry collection -objects’ attributes and functions

# Convex Hull of our MultiPoint --> https://en.wikipedia.org/wiki/Convex_hull
convex = multi_point.convex_hull

# How many lines do we have inside our MultiLineString?
lines_count = len(multi_line)

# Let's calculate the area of our MultiPolygon
multi_poly_area = multi_poly.area

# We can also access different items inside our geometry collections. We can e.g. access a single polygon from
# our MultiPolygon -object by referring to the index
# Let's calculate the area of our Western hemisphere (with a hole) which is at index 0
west_area = multi_poly[0].area

# We can check if we have a "valid" MultiPolygon. MultiPolygon is thought as valid if the individual polygons
# does notintersect with each other. Here, because the polygons have a common 0-meridian, we should NOT have
# a valid polygon. This can be really useful information when trying to find topological errors from your data
valid = multi_poly.is_valid

print("Convex hull of the points:")
print(convex)

print("Number of lines in MultiLineString:", lines_count)

print("Area of our MultiPolygon:", multi_poly_area)

print("Area of our Western Hemisphere polygon:", west_area)

print("Is polygon valid?: ", valid)

