from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    background = Background((9,9),SolidFill(5))
    new_group_of_shapes.append(background)

    gos_list = group_of_shapes.fetch_shape(['GroupOfShapes'])
    for shapes in gos_list:
        polyline = shapes.fetch_shape(['Polyline'])
        rectangle = shapes.fetch_shape(['Rectangle'])
        normalT = shapes.fetch_shape(['NormalT'])
        invertedT = shapes.fetch_shape(['InvertedT'])
        rightT = shapes.fetch_shape(['RightT'])
        leftT = shapes.fetch_shape(['LeftT'])
        if len(normalT) != 0:
            normalT[0].move_to_edge(background.x_size,background.y_size,'top')
            new_group_of_shapes.append(normalT[0])
        if len(invertedT) != 0:
            invertedT[0].move_to_edge(background.x_size,background.y_size,'bottom')
            new_group_of_shapes.append(invertedT[0])
        if len(rightT) != 0:
            rightT[0].move_to_edge(background.x_size,background.y_size,'left')
            new_group_of_shapes.append(rightT[0])
        if len(leftT) != 0:
            leftT[0].move_to_edge(background.x_size,background.y_size,'right')
            new_group_of_shapes.append(leftT[0])
        if len(polyline) != 0:
            if polyline[0].Lshape_direction() == 'bottom-left-L':
                polyline[0].move_to_edge(background.x_size,background.y_size,'bottom-left')
                new_group_of_shapes.append(polyline[0])
            if polyline[0].Lshape_direction() == 'bottom-right-L':
                polyline[0].move_to_edge(background.x_size,background.y_size,'bottom-right')
                new_group_of_shapes.append(polyline[0])
            if polyline[0].Lshape_direction() == 'top-left-L':
                polyline[0].move_to_edge(background.x_size,background.y_size,'top-left')
                new_group_of_shapes.append(polyline[0])
            if polyline[0].Lshape_direction() == 'top-right-L':
                polyline[0].move_to_edge(background.x_size,background.y_size,'top-right')
                new_group_of_shapes.append(polyline[0])
        

    return (GroupOfShapes(new_group_of_shapes))
