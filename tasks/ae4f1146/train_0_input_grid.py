from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Rectangle(((0,0),(2,2)),SolidFill(8)),
                Dot((1,0),SolidFill(1))
                ]),
            GroupOfShapes([
                Rectangle(((1,4),(3,6)),SolidFill(8)),
                Dot((1,5),SolidFill(1)),
                Dot((2,5),SolidFill(1)),
                Dot((2,4),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((4,1),(6,3)),SolidFill(8)),
                Dot((4,3),SolidFill(1)),
                Dot((6,2),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((5,6),(7,8)),SolidFill(8)),
                Dot((5,7),SolidFill(1)),
                Dot((6,6),SolidFill(1)),
                Dot((7,6),SolidFill(1)),
                Dot((6,8),SolidFill(1)),
                Dot((7,8),SolidFill(1)),
                ]),
			]))
