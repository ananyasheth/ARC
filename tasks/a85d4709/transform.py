from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
   new_group_of_shapes=[Background((3,3))]
   for shape in group_of_shapes.shapes[1:]:
     if shape.min_y == 0:
       new_group_of_shapes.append(Line(((shape.min_x,0),(shape.min_x,2)),SolidFill(2)))
     if shape.min_y == 1:
       new_group_of_shapes.append(Line(((shape.min_x,0),(shape.min_x,2)),SolidFill(4)))
     if shape.min_y == 2:
       new_group_of_shapes.append(Line(((shape.min_x,0),(shape.min_x,2)),SolidFill(3)))
   return (GroupOfShapes(new_group_of_shapes))
    
   
   





