from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    dots = group_of_shapes.fetch_shape(['Dot'])
    
    colour_list =[]
    colour_count = 0
    for dot in dots:
        if dot.fill.colour not in colour_list:
            colour_list.append(dot.fill.colour)
            colour_count +=1
    
    new_background_size = background.x_size * colour_count
    new_group_of_shapes.append(Background((new_background_size,new_background_size)))
    for dot in dots:
        new_reference_dot_x = dot.min_x * colour_count
        new_reference_dot_y = dot.min_y * colour_count
        new_group_of_shapes.append(Rectangle(((new_reference_dot_x,new_reference_dot_y),(new_reference_dot_x+(colour_count-1),new_reference_dot_y+(colour_count-1))),SolidFill(dot.fill.colour)))
    
    return (GroupOfShapes(new_group_of_shapes))
    
   