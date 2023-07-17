from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    dots = group_of_shapes.fetch_shape(['Dot'])
    triangle = group_of_shapes.fetch_shape(['Triangle'])
    triangle_shape = triangle[0] # one triangle in each input


    # Find the range of y coordination of triangle
    traiangle_range_y = [*range(triangle_shape.min_y, triangle_shape.max_y, 1)]

    # Find the x coordination
    triangle_max_x_corr = triangle_shape.max_x


    for dot in dots:
 
        if dot.min_y in traiangle_range_y and dot.min_x >= triangle_max_x_corr:
       
            # Find line starting y coordination
            line_start_y_corr = dot.min_y

            # Find line starting x coordination
            if dot.min_y == triangle_shape.points[1][1]:                # if the dot is in the middle of the triangle
                line_start_x_corr = triangle_max_x_corr-1

            elif dot.min_y == triangle_shape.points[0][1] or dot.min_y == triangle_shape.points[2][1]:          # if the dot is at the edge corner of triangle
                line_start_x_corr = triangle_max_x_corr+1

            else:
                line_start_x_corr = triangle_max_x_corr

            # Create line            
            line = Line(((line_start_x_corr, line_start_y_corr),(background.x_size, line_start_y_corr)),SolidFill(dot.fill.colour))
            new_group_of_shapes.append(line)
    
    return GroupOfShapes(new_group_of_shapes)