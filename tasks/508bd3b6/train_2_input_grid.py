from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
            Background((12,12)),
            Line(((0,0),(11,0)),SolidFill(2)),
            Line(((0,1),(11,1)),SolidFill(2)),
            Line(((9,6),(11,8)),SolidFill(8))
            ]))

