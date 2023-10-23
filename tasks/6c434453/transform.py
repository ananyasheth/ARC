from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = group_of_shapes.fetch_shape(['Background'])
    rectangles = group_of_shapes.fetch_shape(['Rectangle'])
    polylines = group_of_shapes.fetch_shape(['Polyline'])
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    rectangleoutlines = group_of_shapes.fetch_shape(['RectangleOutline'])

    list_of_shapes =[]
    list_of_shapes.extend([background,rectangles,polylines,lines, rectangleoutlines])
    for shapes in list_of_shapes:
        if shapes != rectangleoutlines:
            for shape in shapes:
                new_group_of_shapes.append(shape)
        else:
            for shape in shapes:
                new_group_of_shapes.append(Line(((shape.min_x+1,shape.min_y),(shape.min_x+1, shape.max_y)),SolidFill(2)))
                new_group_of_shapes.append(Line(((shape.min_x,shape.min_y+1),(shape.max_x, shape.min_y+1)),SolidFill(2)))

    

    


    return GroupOfShapes(new_group_of_shapes)
