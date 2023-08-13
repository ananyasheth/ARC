from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((20,20)),
		RectangleOutline(((0,0),(4,4)),SolidFill(1)),
		RectangleOutline(((1,6),(4,9)),SolidFill(1)),
        RectangleOutline(((3,12),(8,17)),SolidFill(1)),
        RectangleOutline(((12,12),(19,19)),SolidFill(1)),
		RectangleOutline(((9,2),(15,8)),SolidFill(1)),
		]))
