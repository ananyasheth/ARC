from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    list_of_points = group_of_shapes.intersection_of_lines(lines)
    rectangles = group_of_shapes.fetch_shape(['Rectangle'])

    x_coor_count = {}
    y_coor_count = {}
    for x, y in list_of_points:
        # Count x coordinates
        if x in x_coor_count:
            x_coor_count[x] += 1
        else:
            x_coor_count[x] = 1

        # Count y coordinates
        if y in y_coor_count:
            y_coor_count[y] += 1
        else:
            y_coor_count[y] = 1
    
    max_x_count = max(x_coor_count.values())
    max_y_count = max(y_coor_count.values())

    new_rectangle = Rectangle(((0,0),(max_y_count,max_x_count)),SolidFill(rectangles[0].fill.colour))
    new_group_of_shapes.append(new_rectangle)


    return(GroupOfShapes(new_group_of_shapes))
