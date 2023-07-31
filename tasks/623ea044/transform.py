from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    dot = group_of_shapes.fetch_shape(['Dot'])
    dot = dot[0]

    line_1 = group_of_shapes.extend((background.x_size, background.y_size),(dot.min_x, dot.min_y), "top-left", dot.fill.colour)
    line_2 = group_of_shapes.extend((background.x_size, background.y_size),(dot.min_x, dot.min_y), "top-right", dot.fill.colour)
    line_3 = group_of_shapes.extend((background.x_size, background.y_size),(dot.min_x, dot.min_y), "bottom-left", dot.fill.colour)
    line_4 = group_of_shapes.extend((background.x_size, background.y_size),(dot.min_x, dot.min_y), "bottom-right", dot.fill.colour)

    new_group_of_shapes.extend([line_1, line_2, line_3, line_4])

    return (GroupOfShapes(new_group_of_shapes))


