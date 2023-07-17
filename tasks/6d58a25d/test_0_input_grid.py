from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    triangle = Triangle(((6,3),(3,6),(6,9)),SolidFill(1))
    tshape = Tshape(((6,4),(6,8),(5,6)),SolidFill(0))
    triangle.delete(tshape)
    return(GroupOfShapes([
        Background((20,20)),
        Dot((8,0),SolidFill(6)),
        Dot((12,1),SolidFill(6)),
        Dot((3,2),SolidFill(6)),
        Dot((1,4),SolidFill(6)),
        Dot((8,4),SolidFill(6)),
        Dot((10,5),SolidFill(6)),
        Dot((7,7),SolidFill(6)),
        Dot((16,7),SolidFill(6)),
        Dot((1,10),SolidFill(6)),
        Dot((19,10),SolidFill(6)),
        Dot((2,11),SolidFill(6)),
        Dot((12,11),SolidFill(6)),
        Dot((5,13),SolidFill(6)),
        Dot((16,14),SolidFill(6)),
        Dot((7,16),SolidFill(6)),
        Dot((12,16),SolidFill(6)),
        Dot((18,17),SolidFill(6)),
        Dot((1,18),SolidFill(6)),
        Dot((5,18),SolidFill(6)),
        Dot((14,18),SolidFill(6)),
        triangle
        ]))
