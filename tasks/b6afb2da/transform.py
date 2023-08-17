from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)

    rectangles = group_of_shapes.fetch_shape(['Rectangle'])
    for rectangle in rectangles:
        rectangle.updateColour(4)
        rectangle.updateCell(rectangle.min_x,rectangle.min_y,1)
        rectangle.updateCell(rectangle.min_x,rectangle.max_y,1)
        rectangle.updateCell(rectangle.max_x,rectangle.min_y,1)
        rectangle.updateCell(rectangle.max_x,rectangle.max_y,1)
        new_group_of_shapes.append(rectangle)
        new_group_of_shapes.append(Rectangle(((rectangle.min_x+1, rectangle.min_y+1),(rectangle.max_x-1, rectangle.max_y-1)),SolidFill(2)))
    
    return (GroupOfShapes(new_group_of_shapes))
    
   
   
