from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes] 
    background = group_of_shapes.fetch_shape(['Background'])[0]
    rectangle = group_of_shapes.fetch_shape(['Rectangle'])[0]
    dots = group_of_shapes.fetch_shape(['Dot'])
    for dot in dots:
        if dot.min_x > rectangle.min_x and dot.min_y > rectangle.min_y:
            line = group_of_shapes.extend((background.x_size, background.y_size), (dot.min_x, dot.min_y), 'bottom-right', dot.fill.colour)
        elif dot.min_x > rectangle.min_x and dot.min_y < rectangle.min_y:
            line = group_of_shapes.extend((background.x_size, background.y_size), (dot.min_x, dot.min_y), 'bottom-left', dot.fill.colour)
        elif dot.min_x < rectangle.min_x and dot.min_y > rectangle.min_y:
            line = group_of_shapes.extend((background.x_size, background.y_size), (dot.min_x, dot.min_y), 'top-right', dot.fill.colour)
        else:
            line = group_of_shapes.extend((background.x_size, background.y_size), (dot.min_x, dot.min_y), 'top-left', dot.fill.colour)
        new_group_of_shapes.append(line)


    return (GroupOfShapes(new_group_of_shapes))
