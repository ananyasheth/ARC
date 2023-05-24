from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
            Background((8,8)),
            Dot((0,7),SolidFill(2)),
            Dot((6,2),SolidFill(2)),
            Dot((2,3),SolidFill(3)),
            Dot((4,6),SolidFill(8))
            ]))

