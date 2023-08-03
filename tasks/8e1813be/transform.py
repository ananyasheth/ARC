from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    Rectangle = group_of_shapes.fetch_shape(['Rectangle'])[0]

    new_bg_size = Rectangle.x_size
    background = Background((new_bg_size,new_bg_size))
    new_group_of_shapes = []
    new_group_of_shapes.append(background)

    lines_colour = [line.fill.colour for line in lines]

    if lines[0].kind == 'HLine':
        for row in range(0,new_bg_size):
            line_colour = lines_colour[row]
            new_group_of_shapes.append(Line(((row,0),(row,new_bg_size)),SolidFill(line_colour)))
    else:
        for column in range(0,new_bg_size):
            line_colour = lines_colour[column]
            new_group_of_shapes.append(Line(((0,column),(new_bg_size,column)),SolidFill(line_colour)))

    return GroupOfShapes(new_group_of_shapes)
       
