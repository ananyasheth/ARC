from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [] 
    new_group_of_shapes.append(group_of_shapes)
    dots = group_of_shapes.fetch_shape(['Dot'])

    if dots[0].fill.colour == 2 :
        if dots[0].min_x < dots[1].min_x and dots[0].min_y < dots[1].min_y:     #
            polyline = Polyline(((dots[0].min_x, dots[0].min_y+1),(dots[0].min_x, dots[1].min_y),(dots[1].min_x-1, dots[1].min_y)),SolidFill(8))

        elif dots[0].min_x < dots[1].min_x and dots[0].min_y > dots[1].min_y:
            polyline = Polyline(((dots[0].min_x, dots[0].min_y-1),(dots[0].min_x, dots[1].min_y),(dots[1].min_x-1, dots[1].min_y)),SolidFill(8))

        elif dots[0].min_x > dots[1].min_x and dots[0].min_y < dots[1].min_y:
            polyline = Polyline(((dots[0].min_x, dots[0].min_y+1),(dots[0].min_x, dots[1].min_y),(dots[1].min_x+1, dots[1].min_y)),SolidFill(8))

        else:
            polyline = Polyline(((dots[0].min_x, dots[0].min_y-1),(dots[0].min_x, dots[1].min_y),(dots[1].min_x+1, dots[1].min_y)),SolidFill(8))

    else:
        if dots[1].min_x < dots[0].min_x and dots[1].min_y < dots[0].min_y:
            polyline = Polyline(((dots[1].min_x, dots[1].min_y+1),(dots[1].min_x, dots[0].min_y),(dots[0].min_x-1, dots[0].min_y)),SolidFill(8))

        elif dots[1].min_x < dots[0].min_x and dots[1].min_y > dots[0].min_y:
                polyline = Polyline(((dots[1].min_x, dots[1].min_y-1),(dots[1].min_x, dots[0].min_y),(dots[0].min_x-1, dots[0].min_y)),SolidFill(8))

        elif dots[1].min_x > dots[0].min_x and dots[1].min_y < dots[0].min_y:
            polyline = Polyline(((dots[1].min_x, dots[1].min_y+1),(dots[1].min_x, dots[0].min_y),(dots[0].min_x+1, dots[0].min_y)),SolidFill(8))

        else:
            polyline = Polyline(((dots[1].min_x, dots[1].min_y-1),(dots[1].min_x, dots[0].min_y),(dots[0].min_x+1, dots[0].min_y)),SolidFill(8))

    new_group_of_shapes.append(polyline)
    
    return (GroupOfShapes(new_group_of_shapes))
