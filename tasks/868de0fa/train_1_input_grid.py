from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		RectangleOutline(((0,0),(2,2)),SolidFill(1)),
		RectangleOutline(((0,4),(5,9)),SolidFill(1)),
		]))
