from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    new_group_of_shapes.append(group_of_shapes)
    rectangles = group_of_shapes.fetch_shape(['Rectangle'])

    for rectangle in rectangles:
        dot_1 = Dot((rectangle.min_x-1, rectangle.min_y-1), SolidFill(1))
        dot_2 = Dot((rectangle.min_x-1, rectangle.max_y+1), SolidFill(2))
        dot_3 = Dot((rectangle.max_x+1, rectangle.min_y-1), SolidFill(3))
        dot_4 = Dot((rectangle.max_x+1, rectangle.max_y+1), SolidFill(4))
        new_group_of_shapes.extend([dot_1, dot_2, dot_3, dot_4])

    return (GroupOfShapes(new_group_of_shapes))
