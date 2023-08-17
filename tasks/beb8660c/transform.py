from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)

    lines = group_of_shapes.fetch_shape(['HLine'])
    lines_sorted = sorted(lines, key=lambda line: line.y_size, reverse=True)
    
    x1=background.x_size-1
    y1=0   
    for line in lines_sorted:
        new_group_of_shapes.append(Line(((x1,y1),(x1,background.y_size-1)),SolidFill(line.fill.colour)))
        x1-=1
        y1+=1
    return (GroupOfShapes(new_group_of_shapes))
    
   