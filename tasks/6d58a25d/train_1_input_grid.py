from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    triangle = Triangle(((8,4),(5,7),(8,10)),SolidFill(7))
    tshape = Tshape(((8,5),(8,9),(7,7),(7,7)),SolidFill(0))
    triangle.delete(tshape)
    return(GroupOfShapes([
        Background((20,20)),
        Dot((18,1),SolidFill(2)),
        Dot((10,1),SolidFill(2)),
        Dot((2,2),SolidFill(2)),
        Dot((1,8),SolidFill(2)),
        Dot((4,13),SolidFill(2)),
        Dot((4,16),SolidFill(2)),
        Dot((9,17),SolidFill(2)),
        Dot((14,16),SolidFill(2)),
        Dot((17,14),SolidFill(2)),
        Dot((10,9),SolidFill(2)),
        Dot((12,6),SolidFill(2)),
        triangle
        ]))
