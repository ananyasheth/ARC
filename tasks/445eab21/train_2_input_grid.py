from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			RectangleOutline(((0,1),(6,6)),SolidFill(4)),
			RectangleOutline(((7,7),(9,9)),SolidFill(2))
			]))