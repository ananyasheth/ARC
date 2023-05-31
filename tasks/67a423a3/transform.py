from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    lines = group_of_shapes.fetch_shape(['HLine','VLine','DLine'])
    list_of_points = group_of_shapes.intersection_of_lines(lines)
    if len(list_of_points)==1:
      point1,point2=list_of_points[0][0],list_of_points[0][1]
    new_rectangle = RectangleOutline(((point1-1,point2-1),(point1+1,point2+1)),SolidFill(4))
    return(GroupOfShapes([group_of_shapes,new_rectangle]))
