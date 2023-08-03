from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    line = group_of_shapes.fetch_shape(kind=['HLine'])[0]
    new_group_of_shapes.extend([background, line])

    dots_grey = group_of_shapes.fetch_shape(kind=['Dot'], colour=[5])
    for dot in dots_grey:
        new_group_of_shapes.append(dot)
        new_group_of_shapes.append(Dot((dot.min_x+1, dot.min_y),SolidFill(1)))
    return GroupOfShapes(new_group_of_shapes)

