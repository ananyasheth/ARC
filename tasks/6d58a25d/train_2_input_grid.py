from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    triangle = Triangle(((7,9),(4,12),(7,15)),SolidFill(4))
    tshape = Tshape(((7,10),(7,14),(6,12)),SolidFill(0))
    triangle.delete(tshape)
    return(GroupOfShapes([
        Background((20,20)),
        Dot((17,1),SolidFill(3)),
        Dot((12,0),SolidFill(3)),
        Dot((4,1),SolidFill(3)),
        Dot((10,2),SolidFill(3)),
        Dot((7,4),SolidFill(3)),
        Dot((15,4),SolidFill(3)),
        Dot((2,5),SolidFill(3)),
        Dot((5,7),SolidFill(3)),
        Dot((12,7),SolidFill(3)),
        Dot((18,7),SolidFill(3)),
        Dot((2,10),SolidFill(3)),
        Dot((9,10),SolidFill(3)),
        Dot((16,12),SolidFill(3)),
        Dot((18,13),SolidFill(3)),
        Dot((12,13),SolidFill(3)),
        Dot((1,14),SolidFill(3)),
        Dot((17,16),SolidFill(3)),
        Dot((12,18),SolidFill(3)),
        Dot((5,18),SolidFill(3)),
        Dot((18,19),SolidFill(3)),
        triangle
        ]))
