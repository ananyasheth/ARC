from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Rectangle(((1,0),(3,2)),SolidFill(8)),
                ]),
            GroupOfShapes([
                Rectangle(((0,4),(2,6)),SolidFill(8)),
                Dot((2,4),SolidFill(1))
                ]),
            GroupOfShapes([
                Rectangle(((5,0),(7,2)),SolidFill(8)),
                Dot((5,1),SolidFill(1)),
                Dot((6,2),SolidFill(1)),
                Dot((7,0),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((4,6),(6,8)),SolidFill(8)),
                Dot((4,7),SolidFill(1)),
                Dot((5,7),SolidFill(1)),
                Dot((5,6),SolidFill(1)),
                Dot((6,6),SolidFill(1)),
                Dot((6,8),SolidFill(1)),
                ]),
			]))
