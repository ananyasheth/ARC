from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((11,11)),
		RectangleOutline(((1,1),(3,3)),SolidFill(1)),
		RectangleOutline(((6,0),(10,4)),SolidFill(1)),
        RectangleOutline(((2,5),(5,8)),SolidFill(1)),
		]))
