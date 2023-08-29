from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    gos_list = group_of_shapes.fetch_shape(['GroupOfShapes'])
    max_dot_count = 0
    largest_shape_index = None
    for index, shapes in enumerate(gos_list):
        dots = shapes.fetch_shape(['Dot'])
        if len(dots) > max_dot_count:
            max_dot_count = len(dots)
            largest_shape_index = index
    largest_shape = gos_list[largest_shape_index]
    new_group_of_shapes.append(largest_shape)
    return GroupOfShapes(new_group_of_shapes)
       
