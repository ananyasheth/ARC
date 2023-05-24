from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((2,6)),
			Line(((0,0),(0,5)),SolidFill(4)),
			Line(((1,0),(1,5)),SolidFill(8))
			]))

