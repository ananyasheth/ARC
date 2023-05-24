from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			RectangleOutline(((0,1),(3,4)),SolidFill(7)),
			RectangleOutline(((5,3),(8,7)),SolidFill(8)),
			]))