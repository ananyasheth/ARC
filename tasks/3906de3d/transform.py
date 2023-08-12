from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    new_group_of_shapes.append(background)
    lines_blue = group_of_shapes.fetch_shape(kind=['HLine','VLine'],colour=[1])
    lines_red = group_of_shapes.fetch_shape(kind=['HLine','VLine'],colour=[2])

    for line_blue in lines_blue:
        new_group_of_shapes.append(line_blue)
   
        for line_red in lines_red:
            if line_red.min_y == line_blue.min_y:
                line_red.move_by(-(line_red.min_x-(line_blue.max_x+1)),0)
                new_group_of_shapes.append(line_red)
                

    return (GroupOfShapes(new_group_of_shapes))
