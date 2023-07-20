from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]

    # fetch C shape polyline
    polyline = group_of_shapes.fetch_shape(['Polyline'])
    polyline_shape = polyline[0] # one polyline in each input



    # locate the firstpoint and lastpoint of C shape
    polyline_firstpoint_x_corr = polyline_shape.points[0][0]
    polyline_firstpoint_y_corr = polyline_shape.points[0][1]
    polyline_lastpoint_x_corr = polyline_shape.points[-1][0]
    polyline_lastpoint_y_corr = polyline_shape.points[-1][1]

    # Create a function to find the lastpoint of diagional line
    def find_last_point_of_diagonal(size, start_x, start_y, direction):
        x, y = start_x, start_y

        # Iterate to find the last point of the diagonal line based on the direction
        if direction == "top-left":
            while x > 0 and y > 0:
                x -= 1
                y -= 1
        elif direction == "top-right":
            while x > 0 and y < size - 1:
                x -= 1
                y += 1
        elif direction == "bottom-left":
            while x < size - 1 and y > 0:
                x += 1
                y -= 1
        elif direction == "bottom-right":
            while x < size - 1 and y < size - 1:
                x += 1
                y += 1
        return (x, y)



    if polyline_lastpoint_x_corr == polyline_firstpoint_x_corr:
        if polyline_lastpoint_x_corr > polyline_shape.min_x:         # downward 

            # Tshape
            x1,y1 = polyline_shape.min_x +1, polyline_shape.min_y+1
            x2,y2 = polyline_lastpoint_x_corr -1, polyline_lastpoint_y_corr
            x3,y3 = polyline_firstpoint_x_corr, polyline_firstpoint_y_corr +1
            x4,y4 = background.x_size, polyline_lastpoint_y_corr -1

            tshape = Tshape(((x1, y1),(x2, y2), (x3, y3), (x4,y4)), SolidFill(4))

            # bottom right diagonal line
            line_first_point = (polyline_lastpoint_x_corr +1, polyline_lastpoint_y_corr)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_lastpoint_x_corr + 1, polyline_lastpoint_y_corr, "bottom-right")
            line = Line((line_first_point,line_last_point),SolidFill(4))


            # bottom left diagonal line
            line_first_point = (polyline_firstpoint_x_corr +1, polyline_firstpoint_y_corr)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_firstpoint_x_corr + 1, polyline_firstpoint_y_corr, "bottom-left")
            line_2 = Line((line_first_point,line_last_point),SolidFill(4))

        else:                                               # upward

            # Tshape
            x1,y1 = polyline_firstpoint_x_corr +1, polyline_firstpoint_y_corr
            x2,y2 = polyline_shape.max_x -1, polyline_shape.max_y -1
            x3,y3 = 0, polyline_lastpoint_y_corr -1
            x4,y4 = polyline_firstpoint_x_corr, polyline_firstpoint_y_corr +1

            tshape = Tshape(((x1, y1),(x2, y2), (x3, y3), (x4,y4)), SolidFill(4))

            # Top right diagonal line
            line_first_point = (polyline_lastpoint_x_corr -1, polyline_lastpoint_y_corr)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_lastpoint_x_corr -1, polyline_lastpoint_y_corr, "top-right")
            line = Line((line_first_point,line_last_point),SolidFill(4))


            # Top left diagonal line
            line_first_point = (polyline_firstpoint_x_corr -1, polyline_firstpoint_y_corr)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_firstpoint_x_corr -1, polyline_firstpoint_y_corr, "top-left")
            line_2 = Line((line_first_point,line_last_point),SolidFill(4))

            
    else:
        if polyline_lastpoint_y_corr > polyline_shape.min_y:         # right

            # Tshape
            x1,y1 = polyline_shape.min_x +1, polyline_shape.min_y+1
            x2,y2 = polyline_lastpoint_x_corr, polyline_lastpoint_y_corr -1
            x3,y3 = polyline_firstpoint_x_corr+1, polyline_firstpoint_y_corr
            x4,y4 = polyline_lastpoint_x_corr -1, background.y_size

            tshape = Tshape(((x1, y1),(x2, y2), (x3, y3), (x4,y4)), SolidFill(4))

            # Top right diagonal line
            line_first_point = (polyline_firstpoint_x_corr, polyline_firstpoint_y_corr+1)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_firstpoint_x_corr, polyline_firstpoint_y_corr+1, "top-right")
            line = Line((line_first_point,line_last_point),SolidFill(4))

            # bottom right diagonal line
            line_first_point = (polyline_lastpoint_x_corr, polyline_lastpoint_y_corr+1)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_lastpoint_x_corr, polyline_lastpoint_y_corr+1, "bottom-right")
            line_2 = Line((line_first_point,line_last_point),SolidFill(4))


        else:                               # left
            
            # Tshape
            x1,y1 = polyline_firstpoint_x_corr, polyline_firstpoint_y_corr +1
            x2,y2 = polyline_shape.max_x -1, polyline_shape.max_y-1
            x3,y3 = polyline_firstpoint_x_corr +1, 0
            x4,y4 = polyline_lastpoint_x_corr-1, polyline_lastpoint_y_corr

            tshape = Tshape(((x1, y1),(x2, y2), (x3, y3), (x4,y4)), SolidFill(4))


            # Top left diagonal line
            line_first_point = (polyline_firstpoint_x_corr, polyline_firstpoint_y_corr-1)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_firstpoint_x_corr, polyline_firstpoint_y_corr-1, "top-left")
            line = Line((line_first_point,line_last_point),SolidFill(4))

            # bottom left diagonal line
            line_first_point = (polyline_lastpoint_x_corr, polyline_lastpoint_y_corr-1)
            line_last_point = find_last_point_of_diagonal(background.x_size, polyline_lastpoint_x_corr, polyline_lastpoint_y_corr-1, "bottom-left")
            line_2 = Line((line_first_point,line_last_point),SolidFill(4))


    new_group_of_shapes.extend([tshape, line, line_2])




    return GroupOfShapes(new_group_of_shapes)
