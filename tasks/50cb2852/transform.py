from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    rectangles = group_of_shapes.fetch_shape(kind=['Rectangle'])

    for rectangle in rectangles:
        new_group_of_shapes.append(Rectangle(((rectangle.min_x+1, rectangle.min_y+1),(rectangle.max_x-1, rectangle.max_y-1)),SolidFill(8)))
    return GroupOfShapes(new_group_of_shapes)
