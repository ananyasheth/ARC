from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]

    new_group_of_shapes.append(background)

    # fetch polyline
    polylines = group_of_shapes.fetch_shape(['Polyline'])
    
    
    for polyline in polylines:
        x1, y1 = polyline.points[0][0], polyline.points[0][1] + 1
        x2, y2 = polyline.points[1][0], polyline.points[1][1] + 1
        x3, y3 = polyline.points[2][0] - 1 , polyline.points[2][1]
        x4, y4 = polyline.points[3][0], polyline.points[3][1]
        x5, y5 = polyline.points[4][0], polyline.points[4][1]
        x6, y6 = x5 -1, y5
        x7, y7 = polyline.points[5][0], polyline.points[5][1] + 1

        new_polyline = Polyline(((x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7)),SolidFill(polyline.fill.colour))
        new_group_of_shapes.append(new_polyline)

    return (GroupOfShapes(new_group_of_shapes))
