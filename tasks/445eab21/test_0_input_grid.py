from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			RectangleOutline(((0,0),(8,4)),SolidFill(3)),
			RectangleOutline(((0,6),(9,9)),SolidFill(9))
			]))