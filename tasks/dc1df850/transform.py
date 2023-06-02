from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    dots = group_of_shapes.fetch_shape(['Dot'])
    if type(dots)!=list:
      dots = [dots]
    for each_dot in dots:
      if each_dot.fill.colour == 2:
        new_group_of_shapes.append(RectangleOutline(((each_dot.min_x-1,each_dot.min_y-1),(each_dot.max_x+1,each_dot.max_y+1)),SolidFill(1)))
    return (GroupOfShapes(new_group_of_shapes))

