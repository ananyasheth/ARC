from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		RectangleOutline(((0,0),(3,3)),SolidFill(1)),
		RectangleOutline(((5,0),(9,4)),SolidFill(1)),
        RectangleOutline(((2,6),(4,8)),SolidFill(1)),
		]))
