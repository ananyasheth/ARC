from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    borderpoints = []
    b_min_x, b_max_x = background.min_x, background.max_x
    b_min_y, b_max_y = background.min_y, background.max_y
    dots = group_of_shapes.fetch_shape(['Dot'])
    if type(dots)!=list:
      dots = [dots]
    for y in (b_min_y,b_max_y):
      borderpoints.extend([(x, y) for x in range(b_min_x, b_max_x + 1)])
    for x in (b_min_x,b_max_x):
      borderpoints.extend([(x, y) for y in range(b_min_y + 1, b_max_y)])
    for each_dot in dots:
      if each_dot.fill.colour == 2:
        if (each_dot.min_x,each_dot.max_x) not in borderpoints:
          new_group_of_shapes.append(RectangleOutline(((each_dot.min_x-1,each_dot.min_y-1),(each_dot.max_x+1,each_dot.max_y+1)),SolidFill(1)))
        else:
          for i in range(each_dot.min_x-1, each_dot.min_x+2):
            for j in range(each_dot.min_y-1, each_dot.min_y+2):
              if  i >= 0 and i < len(background.matrix) and j >= 0 and j < len(background.matrix[0]) and (i,j)!=(each_dot.min_x,each_dot.min_y):
                new_group_of_shapes.append(Dot((i,j),SolidFill(1)))
    return (GroupOfShapes(new_group_of_shapes))
    
