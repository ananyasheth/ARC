from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]
    new_group_of_shapes.append(background)
    rectangle = group_of_shapes.fetch_shape(kind=['Rectangle'])[0]
    new_group_of_shapes.append(rectangle)

    dots = group_of_shapes.fetch_shape(kind=['Dot'])
    moved_dots_list_left =[]
    moved_dots_list_right =[]
    moved_dots_list_top =[]
    moved_dots_list_bottom =[]

    if rectangle.min_x ==0:        # vertical rectangle
        for dot in dots:

            # dots on left side
            if dot.min_y < rectangle.min_y:     
                closest_point = rectangle.min_y
                if dot.min_x not in moved_dots_list_left:
                    dot.move_by(0, (closest_point - 1) - dot.min_y)
                    moved_dots_list_left.append(dot.min_x)
                else:
                    closest_point -= 1
                    dot.move_by(0,(closest_point-1)-dot.min_y)
                    moved_dots_list_left.append(dot.min_x)

            # dots on right side
            else:                                                
                closest_point = rectangle.max_y
                if dot.min_x not in moved_dots_list_right:
                    dot.move_by(0, -(dot.min_y-(closest_point + 1)))
                    moved_dots_list_right.append(dot.min_x)
                else:
                    closest_point += 1
                    dot.move_by(0,-(dot.min_y-(closest_point + 1)))
                    moved_dots_list_right.append(dot.min_x)
            dot.updateColour(5)
            new_group_of_shapes.append(dot)

    
    else:            # horizontal rectangle               
        for dot in dots:

            # dots on top side
            if dot.min_x < rectangle.min_x:     
                closest_point = rectangle.min_x
                if dot.min_y not in moved_dots_list_top:
                    dot.move_by((closest_point - 1) - dot.min_x,0)
                    moved_dots_list_top.append(dot.min_y)
                else:
                    closest_point -= 1
                    dot.move_by((closest_point-1)-dot.min_x,0)
                    moved_dots_list_top.append(dot.min_y)

            # dots on bottom side   
            else:                                             
                closest_point = rectangle.max_x
                if dot.min_y not in moved_dots_list_bottom:
                    dot.move_by(-(dot.min_x-(closest_point + 1)),0)
                    moved_dots_list_bottom.append(dot.min_y)
                else:
                    closest_point += 1
                    dot.move_by(-(dot.min_x-(closest_point + 1)),0)
                    moved_dots_list_bottom.append(dot.min_y)
            dot.updateColour(5)
            new_group_of_shapes.append(dot)

    return (GroupOfShapes(new_group_of_shapes))
