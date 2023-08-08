from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((3,3)),
		Line(((0,0),(0,2)),SolidFill(2)),
		Line(((0,0),(2,0)),SolidFill(2)),
		Dot((1,1),SolidFill(1)),
		Line(((1,2),(2,2)),SolidFill(8)),
		Line(((2,1),(2,2)),SolidFill(8))
		]))
