from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    new_group_of_shapes.append(background)

    # fetch polyline
    dots = group_of_shapes.fetch_shape(['Dot'])
    colour_list = {}
    
    for dot in dots:
        if dot.fill.colour not in colour_list:
            colour_list[dot.fill.colour] = 1
        else:
            colour_list[dot.fill.colour] += 1

    # Find the key with the lowest value in colour_list
    min_colour = min(colour_list, key=lambda k: colour_list[k])

    min_colour_dot = group_of_shapes.fetch_shape(kind=['Dot'],colour=[min_colour])[0]
    new_group_of_shapes.append(min_colour_dot)
    new_group_of_shapes.append(RectangleOutline(((min_colour_dot.min_x-1,min_colour_dot.min_y-1),(min_colour_dot.min_x+1,min_colour_dot.min_y+1)),SolidFill(2)))

    
    return (GroupOfShapes(new_group_of_shapes))
