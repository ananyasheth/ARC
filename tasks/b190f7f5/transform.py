from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    gos_list = group_of_shapes.fetch_shape(['GroupOfShapes'])
    background = group_of_shapes.fetch_shape(['Background'])[0]
    for shapes in gos_list:
        if len(shapes.fetch_shape(['Dot'])) == 0:
            lines = shapes.fetch_shape(['HLine','VLine'])
        else:
            dots = shapes.fetch_shape(['Dot'])
    
    # new background
    if background.x_size <= background.y_size:
        new_background_size_x = background.x_size
    else:
        new_background_size_x = background.y_size
    new_background_size = new_background_size_x*new_background_size_x
    new_group_of_shapes.append(Background((new_background_size,new_background_size)))

    # top-left corner point of line grid
    line_min_x = shapes.return_shape_list_coordinates(lines)[0]
    line_min_y = shapes.return_shape_list_coordinates(lines)[1]
    line_max_x = shapes.return_shape_list_coordinates(lines)[2]
    line_max_y = shapes.return_shape_list_coordinates(lines)[3]
    reference_line_x = line_min_x
    reference_line_y = line_min_y


    # Top-left corner point is the reference point of a 3x3 grid
    dot_min_x = shapes.return_shape_list_coordinates(dots)[0]
    dot_min_y = shapes.return_shape_list_coordinates(dots)[1]
    dot_max_x = shapes.return_shape_list_coordinates(dots)[2]
    dot_max_y = shapes.return_shape_list_coordinates(dots)[3]
    reference_dot_x = dot_min_x
    reference_dot_y = dot_min_y


    # Find the new reference point in new grid
    for dot in dots:
        new_reference_dot_x = (dot.min_x - reference_dot_x)* new_background_size_x
        new_reference_dot_y = (dot.min_y - reference_dot_y)* new_background_size_x

        # line move distance
        move_by_x = new_reference_dot_x - reference_line_x
        move_by_y = new_reference_dot_y - reference_line_y

        # Duplicate new line
        for line in lines:
            newline = line.duplicate(move_by_x,move_by_y)
            newline.updateColour(dot.fill.colour)
            new_group_of_shapes.append(newline)  

    return GroupOfShapes(new_group_of_shapes)
    