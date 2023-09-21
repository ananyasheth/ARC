from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    new_group_of_shapes.append(Background((3,3)))
    gos_list = group_of_shapes.fetch_shape(['GroupOfShapes'])
    for index, gos in enumerate(gos_list):
        rectangles = gos.fetch_shape(['Rectangle'])
        rectangleoutlines = gos.fetch_shape(['RectangleOutline'])
        polylines = gos.fetch_shape(['Polyline'])

        if len(rectangles) ==1:
            line = Line(((index,0),(index,2)),SolidFill(2))
        elif len(rectangles) ==2:
            line = Line(((index,0),(index,2)),SolidFill(4))
        elif len(rectangleoutlines) ==1:
            line = Line(((index,0),(index,2)),SolidFill(8))
        else:
            line = Line(((index,0),(index,2)),SolidFill(3))
        new_group_of_shapes.append(line)
    return(GroupOfShapes(new_group_of_shapes))
