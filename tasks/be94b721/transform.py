from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    polylines = group_of_shapes.fetch_shape(['Polyline'])
    largest_shape = None
    for polyline in polylines:
        if largest_shape is None:
            largest_shape = polyline
        else:
            num_dot = polyline.count_dots()
            if num_dot > largest_shape.count_dots():
                largest_shape = polyline

    largest_shape.matrix[largest_shape.matrix == -1] = 0
    new_group_of_shapes.append(largest_shape)

    return GroupOfShapes(new_group_of_shapes)
       
