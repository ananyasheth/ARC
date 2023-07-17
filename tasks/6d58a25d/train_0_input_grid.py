from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    triangle = Triangle(((8,6),(5,9),(8,12)),SolidFill(9))
    tshape = Tshape(((8,7),(8,11),(7,9)),SolidFill(0))
    triangle.delete(tshape)
    return(GroupOfShapes([
        Background((20,20)),
        Dot((19,1),SolidFill(8)),
        Dot((10,1),SolidFill(8)),
        Dot((4,3),SolidFill(8)),
        Dot((2,5),SolidFill(8)),
        Dot((3,16),SolidFill(8)),
        Dot((10,18),SolidFill(8)),
        Dot((18,15),SolidFill(8)),
        Dot((13,9),SolidFill(8)),
        triangle
        ]))

