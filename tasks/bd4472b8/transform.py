from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    dots = group_of_shapes.fetch_shape(['Dot'])
    background = group_of_shapes.fetch_shape(['Background'])[0]
    dots_colours=[dot.fill.colour for dot in dots]
    dots_colours_length = len(dots_colours)

    for row in range(2, background.x_size):
        current_colour = dots_colours[(row - 2) % dots_colours_length]
        new_group_of_shapes.append(Line(((row,0),(row,background.y_size-1)),SolidFill(current_colour)))
        
        

    return GroupOfShapes(new_group_of_shapes)
       
