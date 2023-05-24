from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):

    new_group_of_shapes=[]
    new_group_of_shapes.append(group_of_shapes)
    mainline = group_of_shapes.fetch_shape(['HLine'])
    for line_number in range(0,mainline.min_x+mainline.y_size):
      if line_number>=mainline.min_x:
        if line_number==mainline.min_x:
          continue
        else:
          new_group_of_shapes.append(Line(((line_number,mainline.min_y),(line_number,mainline.min_x+mainline.y_size-line_number-1)),SolidFill(1)))
      else:
        new_group_of_shapes.append(Line(((line_number,mainline.min_y),(line_number,mainline.min_x+mainline.y_size-line_number-1)),SolidFill(3)))
    return(GroupOfShapes(new_group_of_shapes))
