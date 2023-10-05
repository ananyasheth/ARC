from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    new_group_of_shapes.append(group_of_shapes.fetch_shape(kind=['Background'])[0])
    rectangles = group_of_shapes.fetch_shape(kind=['Rectangle'])
    lines = group_of_shapes.fetch_shape(kind=['HLine', 'VLine'])
    
    for rectangle in rectangles:
        rectangle.updateColour(8)
        new_group_of_shapes.append(rectangle)

    for line in lines:
        line.updateColour(2)
        new_group_of_shapes.append(line)

    return GroupOfShapes(new_group_of_shapes)



