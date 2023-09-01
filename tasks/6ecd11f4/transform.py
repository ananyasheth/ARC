from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *
import math 

def transform(group_of_shapes):
    new_group_of_shapes=[]
    dots = group_of_shapes.fetch_shape(['Dot'])
    rectangles = group_of_shapes.fetch_shape(['Rectangle'])
    background = group_of_shapes.fetch_shape(['Background'])[0]

    # new background
    new_background_size = int(math.sqrt(len(dots)))
    new_background = Background((new_background_size,new_background_size)) 
    new_group_of_shapes.append(new_background)
    
    
    # move all dots to top-left corner
    x_corr_dot = dots[0].min_x
    y_corr_dot = dots[0].min_y
    for dot in dots:
        new_x = 0+abs((x_corr_dot-dot.min_x))
        new_y = 0+abs((y_corr_dot-dot.min_y))
        #print('new_x:',new_x, 'new_y:', new_y)
        dot.move_by(new_x-dot.min_x, new_y-dot.min_y)

    # scale each rectangles
    size = rectangles[0].x_size
    x_corr_rectangle = rectangles[0].min_x
    y_corr_rectangle = rectangles[0].min_y    
    for rectangle in rectangles:
        scale = 1/rectangle.x_size
        rectangle.scale(scale,scale)


    # reform the shape of rectangles
    for rectangle in rectangles[1:]:
        new_x = int(x_corr_rectangle+abs((x_corr_rectangle-rectangle.min_x))/size)
        new_y = int(y_corr_rectangle+abs((y_corr_rectangle-rectangle.min_y))/size)
        rectangle.move_by(new_x-rectangle.min_x, new_y-rectangle.min_y)

    # move rectangles to top-left
    x_corr_rectangle = rectangles[0].min_x 
    
    y_corr_rectangle = rectangles[0].min_y
    for rectangle in rectangles:
        new_x = 0+abs((x_corr_rectangle-rectangle.min_x))
        new_y = 0+abs((y_corr_rectangle-rectangle.min_y))
        rectangle.move_by(new_x-rectangle.min_x, new_y-rectangle.min_y)

        # update rectangle color with dot color
        for dot in dots:
            if rectangle.min_x == dot.min_x and rectangle.min_y == dot.min_y:
                rectangle.updateColour(dot.fill.colour)
        new_group_of_shapes.append(rectangle)

    return (GroupOfShapes(new_group_of_shapes))

