from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
   dots = group_of_shapes.fetch_shape(['Dot'])
   for each_dot in dots:
     each_dot.updateCell(each_dot.max_x,each_dot.max_y,6)
     each_dot.fill.colour=6
     if each_dot.min_y>=3:
       each_dot.min_y=each_dot.min_y-3
       each_dot.max_y=each_dot.max_y-3
       each_dot.y_offset=each_dot.y_offset-3
   dots.insert(0, Background((3,3)))
   return(GroupOfShapes(dots))
   
    
    
   
   





