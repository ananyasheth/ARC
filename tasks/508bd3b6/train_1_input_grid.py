from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
            Background((12,12)),
            Line(((9,0),(9,11)),SolidFill(2)),
            Line(((10,0),(10,11)),SolidFill(2)),
            Line(((11,0),(11,11)),SolidFill(2)),
            Line(((2,0),(4,2)),SolidFill(8))
            ]))

