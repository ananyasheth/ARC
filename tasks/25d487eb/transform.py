from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]       # only one background    
    dots = group_of_shapes.fetch_shape(['Dot'])
    dot = dots[0]                    # only one dot
    triangles = group_of_shapes.fetch_shape(['Triangle'])
    triangle = triangles[0]         # only one triangle


    if triangle.points[0][0] == triangle.points[1][0]:  
        if triangle.points[2][0] < triangle.points[0][0]:   # normal
            line = Line(((triangle.points[2][0]-1, triangle.points[2][1]),(0, triangle.points[2][1])),SolidFill(dot.fill.colour))
        else:                                               # inverted
            line = Line(((triangle.points[2][0]+1, triangle.points[2][1]),(background.x_size, triangle.points[2][1])),SolidFill(dot.fill.colour))
    else:                                               
        if triangle.points[2][1] < triangle.points[0][1]:   # left
            line = Line(((triangle.points[2][0], triangle.points[2][1]-1),(triangle.points[2][0], 0)),SolidFill(dot.fill.colour))
        else:                                               # right
            line = Line(((triangle.points[2][0], triangle.points[2][1]+1),(triangle.points[2][0], background.y_size)),SolidFill(dot.fill.colour))

    new_group_of_shapes.append(line)
    return (GroupOfShapes(new_group_of_shapes))
