from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
   background = group_of_shapes.fetch_shape(['Background'])
   rectangle_outline = RectangleOutline(((0,0),(background.max_x,background.max_y)),SolidFill(8))
   return (GroupOfShapes([background,rectangle_outline]))
     
    
   
   





