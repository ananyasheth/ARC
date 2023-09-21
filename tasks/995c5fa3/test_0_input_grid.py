from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,14)),
            GroupOfShapes([
                Rectangle(((0,0),(3,3)),SolidFill(5)),
                Rectangle(((2,1),(3,2)),SolidFill(0)),
            ]),
            GroupOfShapes([
                Polyline(((0,5),(0,8),(1,7),(2,7),(3,8),(3,5),(2,6),(1,6)),SolidFill(5))
            ]),
            GroupOfShapes([
                RectangleOutline(((0,10),(3,13)),SolidFill(5))
            ]),
			]))