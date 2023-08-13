from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((20,20)),
		RectangleOutline(((2,1),(9,8)),SolidFill(1)),
		RectangleOutline(((11,1),(17,7)),SolidFill(1)),
        RectangleOutline(((0,12),(4,16)),SolidFill(1)),
        RectangleOutline(((7,10),(16,19)),SolidFill(1)),
		]))
