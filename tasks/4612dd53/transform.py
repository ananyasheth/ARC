from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    new_group_of_shapes.append(background)
    rectangle = group_of_shapes.fetch_shape(kind=['RectangleOutline'], colour=[1])[0]
    new_group_of_shapes.append(rectangle)

    lines_blue = group_of_shapes.fetch_shape(kind=['HLine','VLine'],colour=[1])
    for line in lines_blue:
        new_group_of_shapes.append(line)


    dots_black = group_of_shapes.fetch_shape(kind=['Dot'],colour=[0])
    lines_black = group_of_shapes.fetch_shape(kind=['HLine','VLine'],colour=[0])

    for dot in dots_black:
        dot.updateColour(2)
        new_group_of_shapes.append(dot)
    for line in lines_black:
        line.updateColour(2)
        new_group_of_shapes.append(line)
    
    return (GroupOfShapes(new_group_of_shapes))
