from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((3,3)),
		Line(((0,0),(0,2)),SolidFill(2)),
		Line(((0,2),(2,2)),SolidFill(2)),
		Line(((2,0),(2,2)),SolidFill(2)),
		Line(((1,0),(1,1)),SolidFill(8))
		]))
