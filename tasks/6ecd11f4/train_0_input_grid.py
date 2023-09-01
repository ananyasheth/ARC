from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((27,21)),
            Rectangle(((1,1),(5,5)),SolidFill(1)),
            Rectangle(((6,6),(10,10)),SolidFill(1)),
            Rectangle(((5,11),(1,15)),SolidFill(1)),
            Rectangle(((11,5),(15,1)),SolidFill(1)),
            Rectangle(((11,11),(15,15)),SolidFill(1)),
            Dot((19,7),SolidFill(3)),
            Dot((19,8),SolidFill(1)),
            Dot((19,9),SolidFill(7)),
            Dot((20,7),SolidFill(2)),
            Dot((20,8),SolidFill(8)),
            Dot((20,9),SolidFill(9)),
            Dot((21,7),SolidFill(3)),
            Dot((21,8),SolidFill(4)),
            Dot((21,9),SolidFill(6)),
			]))
