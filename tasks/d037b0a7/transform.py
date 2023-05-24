from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
     new_group_of_shapes = []
     background = group_of_shapes.fetch_shape(['Background'])
     new_group_of_shapes.append(background)
     for shape in group_of_shapes.shapes[1:]:
       new_group_of_shapes.append(Line(((shape.min_x,shape.min_y),(background.max_x,shape.max_y)),SolidFill(shape.fill.colour)))
     return GroupOfShapes(new_group_of_shapes)
       
