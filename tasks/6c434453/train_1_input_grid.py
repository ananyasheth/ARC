from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		Rectangle(((1,0),(2,1)),SolidFill(1)),
        RectangleOutline(((0,4),(2,6)),SolidFill(1)),
        RectangleOutline(((5,1),(7,3)),SolidFill(1)),
        Polyline(((3,8),(4,9),(5,8),(4,7),(4,8)),SolidFill(1)),
        Polyline(((7,6),(8,6),(8,7),(8,8)),SolidFill(1)),
		]))
