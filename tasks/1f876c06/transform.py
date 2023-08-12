from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    dots = group_of_shapes.fetch_shape(['Dot'])
    for current_dot in dots:
        for next_dot in dots[1:]:
            if next_dot.fill.colour == current_dot.fill.colour:
                new_group_of_shapes.append(Line(((current_dot.min_x, current_dot.min_y),(next_dot.min_x,next_dot.min_y)),SolidFill(current_dot.fill.colour)))

    return GroupOfShapes(new_group_of_shapes)
