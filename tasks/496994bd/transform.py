from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    new_group_of_shapes.append(group_of_shapes)
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    lines = group_of_shapes.fetch_shape(kind=['HLine'])

    for line in lines:
        line.flip('Horizontal',(background.x_size-1,0))
        new_group_of_shapes.append(line)

   
    return (GroupOfShapes(new_group_of_shapes))
