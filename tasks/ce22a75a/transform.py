from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)
    dots = group_of_shapes.fetch_shape(['Dot'])
    for dot in dots:
        new_group_of_shapes.append(Rectangle(((dot.min_x-1,dot.min_y-1),(dot.min_x+1,dot.min_y+1)),SolidFill(1)))
    
    return (GroupOfShapes(new_group_of_shapes))
    
   
   
