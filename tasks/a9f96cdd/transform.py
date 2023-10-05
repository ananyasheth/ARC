from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    
    dot = group_of_shapes.fetch_shape(['Dot'])[0]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)

    
    new_group_of_shapes.append(Dot((dot.min_x-1,dot.min_y-1),SolidFill(3)))
    new_group_of_shapes.append(Dot((dot.min_x-1,dot.min_y+1),SolidFill(6)))
    new_group_of_shapes.append(Dot((dot.min_x+1,dot.min_y-1),SolidFill(8)))
    new_group_of_shapes.append(Dot((dot.min_x+1,dot.min_y+1),SolidFill(7)))
    
      
    return (GroupOfShapes(new_group_of_shapes))
