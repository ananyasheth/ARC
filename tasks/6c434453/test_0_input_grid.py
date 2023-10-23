from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		RectangleOutline(((2,1),(4,3)),SolidFill(1)),
        RectangleOutline(((7,1),(9,3)),SolidFill(1)),
        Polyline(((0,8),(1,9),(2,8),(1,7),(1,8)),SolidFill(1)),
        Line(((6,6),(6,7)),SolidFill(1)),
        Rectangle(((8,8),(9,9)),SolidFill(1)),
		]))
