from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((27,25)),
            Rectangle(((3,9),(5,11)),SolidFill(3)),
            Rectangle(((6,9),(8,11)),SolidFill(3)),
            Rectangle(((6,12),(8,14)),SolidFill(3)),
            Rectangle(((9,12),(11,14)),SolidFill(3)),
            Rectangle(((9,15),(11,17)),SolidFill(3)),
            Rectangle(((3,15),(5,17)),SolidFill(3)),
            Dot((19,8),SolidFill(2)),
            Dot((19,9),SolidFill(1)),
            Dot((19,10),SolidFill(7)),
            Dot((20,8),SolidFill(4)),
            Dot((20,9),SolidFill(8)),
            Dot((20,10),SolidFill(9)),
            Dot((21,8),SolidFill(8)),
            Dot((21,9),SolidFill(6)),
            Dot((21,10),SolidFill(1)),

            ]))
