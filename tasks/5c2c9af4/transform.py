from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    dots = group_of_shapes.fetch_shape(['Dot'])
    dots_width =  abs(dots[1].min_y-dots[0].min_y)  # distance between each dots
    line_width = dots_width                         # the line from end point to middle point width in each loop

    new_group_of_shapes.append(background)
    new_group_of_shapes.append(dots[1])
    
    # deine points
    (x,y) = (dots[1].min_x, dots[1].min_y)
    (x1,y1) = (x,y) # top
    (x2,y2) = (x,y) # bottom
    (x3,y3) = (x,y) # left
    (x4,y4) = (x,y) # right
    
    bg_size = background.x_size

    loop_count_max = loop_count_1= loop_count_2 = loop_count_3 =loop_count_4 =0
    while x1 >= 0: # Top
        x1 -= dots_width    # move one layer outside
        if x1 >=0:
            loop_count_1 +=1

    while x2 < bg_size: # bottom
        x2 += dots_width
        if x2 <bg_size:
            loop_count_2 +=1

    while y3 >= 0: # left
        y3 -= dots_width
        if y3 >=0:
            loop_count_3 +=1        

    while y4 < bg_size: # right
        y4 += dots_width
        if y4 < bg_size:
            loop_count_4 +=1

    loop_count_max = max(loop_count_1, loop_count_2, loop_count_3, loop_count_4)
    for loop in range(0,loop_count_max):
        new_group_of_shapes.append(RectangleOutline(((x-line_width,y-line_width),(x+line_width,y+line_width)),SolidFill(dots[1].fill.colour)))
        line_width += dots_width

    return GroupOfShapes(new_group_of_shapes)
