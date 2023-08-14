from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    new_line_list = []

    for line in lines:
        if line.min_x == 0:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.min_y), 'bottom',line.fill.colour)
        elif line.max_x == background.x_size-1:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.max_x,line.min_y), 'top',line.fill.colour)
        elif line.min_y == 0:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.min_y), 'right',line.fill.colour)
        else:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.max_y), 'left',line.fill.colour)           

        new_group_of_shapes.append(new_line)
        new_line_list.append(new_line)
        intersection_point = group_of_shapes.intersection_of_lines(new_line_list)

    new_group_of_shapes.append(Dot((intersection_point[0][0],intersection_point[0][1]),SolidFill(4)))
    
    return(GroupOfShapes(new_group_of_shapes))
