from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			RectangleOutline(((0,0),(3,4)),SolidFill(6)),
			RectangleOutline(((5,2),(8,7)),SolidFill(7))
			]))