from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    new_group_of_shapes.append(background)
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    for line in lines:
        if line.min_x == 0:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.min_y), 'bottom',line.fill.colour)
            intersection_point_y = line.min_y
        elif line.max_x == background.x_size-1:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.max_x,line.min_y), 'top',line.fill.colour)
            intersection_point_y = line.min_y
        elif line.min_y == 0:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.min_y), 'right',line.fill.colour)
            intersection_point_x = line.min_x
        else:
            new_line = group_of_shapes.extend((background.x_size, background.y_size),(line.min_x,line.max_y), 'left',line.fill.colour)
            intersection_point_x = line.min_x
        new_group_of_shapes.append(new_line)
    new_group_of_shapes.append(Dot((intersection_point_x,intersection_point_y),SolidFill(4)))
    
    #print(intersection_points)
    return(GroupOfShapes(new_group_of_shapes))
