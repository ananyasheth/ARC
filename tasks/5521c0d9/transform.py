from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    new_group_of_shapes.append(background)
    rectangles = group_of_shapes.fetch_shape(kind=['Rectangle'])

    for rectangle in rectangles:
        rectangle.move_by(-rectangle.x_size,0)
        new_group_of_shapes.append(rectangle)
  
    return (GroupOfShapes(new_group_of_shapes))
