from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,14)),
            GroupOfShapes([
                Rectangle(((0,0),(3,3)),SolidFill(5))
            ]),
            GroupOfShapes([
                RectangleOutline(((0,5),(3,8)),SolidFill(5))
            ]),
            GroupOfShapes([
                Polyline(((0,10),(0,13),(1,12),(2,12),(3,13),(3,10),(2,11),(1,11)),SolidFill(5))
            ])
			]))