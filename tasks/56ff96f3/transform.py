from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
   new_group_of_shapes=[]
   new_group_of_shapes.append(group_of_shapes)
   dots = group_of_shapes.fetch_shape(['Dot'])
   for dot in dots:
     for next_dot in dots[1:]:
       if dot.fill.colour == next_dot.fill.colour:
         new_group_of_shapes.append(Rectangle(((dot.min_x,dot.min_y),(next_dot.min_x,next_dot.min_y)),SolidFill(dot.fill.colour)))
   return (GroupOfShapes(new_group_of_shapes))
     
    
   
   





