from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    dots = group_of_shapes.fetch_shape(['Dot'])
    dots_h = []
    dots_v = []

    for dot in dots:
        if dot.min_x == 0:
            dots_h.append(dot)
        else:
            dots_v.append(dot)
    
    for dot_h in dots_h:
        for dot_v in dots_v:
            new_group_of_shapes.append(Dot((dot_v.min_x, dot_h.min_y), SolidFill(2)))

    return GroupOfShapes(new_group_of_shapes)

