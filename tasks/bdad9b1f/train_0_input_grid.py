from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,6)),
			Line(((2,0),(2,1)),SolidFill(2)),
			Line(((0,4),(1,4)),SolidFill(8))
			]))
