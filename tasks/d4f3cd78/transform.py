from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    polyline = group_of_shapes.fetch_shape(['Polyline'])
    polyline_shape = polyline[0] # one polyline in each input
    rectanglefill = Rectangle(((polyline_shape.min_x + 1, polyline_shape.min_y + 1), (polyline_shape.max_x - 1, polyline_shape.max_y - 1)), SolidFill(8))

    firstpoint_x_corr = polyline_shape.points[0][0]
    firstpoint_y_corr = polyline_shape.points[0][1]
    lastpoint_x_corr = polyline_shape.points[-1][0]
    lastpoint_y_corr = polyline_shape.points[-1][1]

    
    if lastpoint_x_corr == firstpoint_x_corr:
        if lastpoint_x_corr > polyline_shape.min_x:         # downward 
            line = Line(((firstpoint_x_corr, firstpoint_y_corr+1), (background.x_size, firstpoint_y_corr+1)), SolidFill(8))
        else:                                               # upward
            line = Line(((firstpoint_x_corr, firstpoint_y_corr+1), (0, firstpoint_y_corr+1)), SolidFill(8))            
    else:
        if lastpoint_y_corr > polyline_shape.min_y:         # right
            line = Line(((firstpoint_x_corr+1, firstpoint_y_corr),(firstpoint_x_corr+1, background.y_size)), SolidFill(8))
        else:
            line = Line(((firstpoint_x_corr+1, firstpoint_y_corr),(firstpoint_x_corr+1, 0)), SolidFill(8))         

    new_group_of_shapes.extend([rectanglefill, line])
    return GroupOfShapes(new_group_of_shapes)
       
