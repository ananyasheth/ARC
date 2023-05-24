from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,6)),
			Line(((2,0),(2,5)),SolidFill(9)),
			Line(((0,2),(5,2)),SolidFill(1))
			]))
