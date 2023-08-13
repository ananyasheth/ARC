from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((15,15)),
		RectangleOutline(((1,1),(7,7)),SolidFill(1)),
		RectangleOutline(((9,6),(14,11)),SolidFill(1)),
		]))
