from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
            Background((12,12)),
            Line(((0,11),(11,11)),SolidFill(2)),
            Line(((0,10),(11,10)),SolidFill(2)),
            Line(((0,9),(11,9)),SolidFill(2)),
            Line(((0,8),(11,8)),SolidFill(2)),
            Line(((0,3),(1,4)),SolidFill(8))
            ]))

