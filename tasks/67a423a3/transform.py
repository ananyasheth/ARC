from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    lines = group_of_shapes.fetch_shape(['HLine','VLine','DLine'])
    point1,point2 = group_of_shapes.intersection_of_lines(lines)
    new_rectangle = RectangleOutline(((point1-1,point2-1),(point1+1,point2+1)),SolidFill(4))
    return(GroupOfShapes([group_of_shapes,new_rectangle]))
	
