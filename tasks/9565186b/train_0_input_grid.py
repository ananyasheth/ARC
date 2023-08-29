from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((3,3)),
		Polyline(((0,2),(0,0),(2,0)),SolidFill(2)),
		Dot((1,1),SolidFill(1)),
		Polyline(((1,2),(2,2),(2,1)),SolidFill(8)),
		]))
