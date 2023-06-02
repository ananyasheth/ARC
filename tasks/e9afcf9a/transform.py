from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    i=0
    lines = group_of_shapes.fetch_shape(['HLine'])
    line_colours=[line.fill.colour for line in lines]
    new_group_of_shapes=group_of_shapes.fetch_shape(['Background'])
    for line in lines:
      if i%2==0:
        new_group_of_shapes.append(Line(((line.min_x,line.min_y),(line.max_x,line.max_y)),CheckeredFill(line_colours)))
      else:
        line_colours.reverse()
        new_group_of_shapes.append(Line(((line.min_x,line.min_y),(line.max_x,line.max_y)),CheckeredFill(line_colours)))
        line_colours.reverse()
      i+=1
    return(GroupOfShapes(new_group_of_shapes))
    
