from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		RectangleOutline(((0,0),(2,2)),SolidFill(1)),
        Polyline(((4,1),(5,2),(6,1),(5,0),(5,1)),SolidFill(1)),
        RectangleOutline(((6,3),(8,5)),SolidFill(1)),
        Polyline(((1,7),(2,8),(3,7),(2,6),(2,7)),SolidFill(1)),
        Line(((7,8),(7,9)),SolidFill(1)),
		]))
