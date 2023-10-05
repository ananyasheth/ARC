from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = Background((3,6))
    new_group_of_shapes.append(background)
    dots = group_of_shapes.fetch_shape(['Dot'])
    
    for dot in dots:
        new_group_of_shapes.append(dot)
        new_dot = Dot((dot.min_x,dot.min_y),SolidFill(dot.fill.colour))
        new_dot.flip('Vertical',(background.x_size, background.y_size-1))
        new_group_of_shapes.append(new_dot)

    return (GroupOfShapes(new_group_of_shapes))
    
   