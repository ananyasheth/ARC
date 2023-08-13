from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    rectangleOutlines = group_of_shapes.fetch_shape(kind=['RectangleOutline'])

    for rectangleOutline in rectangleOutlines:
        if rectangleOutline.x_size %2 ==0:
            new_group_of_shapes.append(Rectangle(((rectangleOutline.min_x+1, rectangleOutline.min_y+1),(rectangleOutline.max_x-1, rectangleOutline.max_y-1)),SolidFill(2)))
        else:
            new_group_of_shapes.append(Rectangle(((rectangleOutline.min_x+1, rectangleOutline.min_y+1),(rectangleOutline.max_x-1, rectangleOutline.max_y-1)),SolidFill(7)))
    return GroupOfShapes(new_group_of_shapes)

