from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    new_group_of_shapes.append(background)
    gos_list = group_of_shapes.fetch_shape(['GroupOfShapes'])
    for shapes in gos_list:
        dots = shapes.fetch_shape(['Dot'])
    
    # Top-left corner point is the reference point of a 3x3 grid
    reference_dot_x = None
    reference_dot_y = None
    for dot in dots:
        if reference_dot_x is None:
            reference_dot_x = dot.min_x
        elif dot.min_x < reference_dot_x:
            reference_dot_x = dot.min_x
        if reference_dot_y is None:
            reference_dot_y = dot.min_y
        elif dot.min_y < reference_dot_y:
            reference_dot_y = dot.min_y

    # Find the new reference point in a 9x9 grid
    for dot in dots:
        new_group_of_shapes.append(dot) 
        new_reference_dot_x = (dot.min_x - reference_dot_x)*3
        new_reference_dot_y = (dot.min_y - reference_dot_y)*3
        move_by_x = new_reference_dot_x - reference_dot_x
        move_by_y = new_reference_dot_y - reference_dot_y

        # New dot
        for dot in dots:
            new_dot = Dot((dot.min_x+move_by_x, dot.min_y+move_by_y), SolidFill(dot.fill.colour))
            new_group_of_shapes.append(new_dot)

    return (GroupOfShapes(new_group_of_shapes))
