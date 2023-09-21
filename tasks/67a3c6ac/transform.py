from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    background = group_of_shapes.fetch_shape(['Background'])[0]
    group_of_shapes.flip('Vertical',(background.x_size, background.y_size-1))
       
    return (group_of_shapes)
     
    
   
   




