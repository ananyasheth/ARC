from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,9)),
			Line(((2,0),(2,3)),SolidFill(2))
			]))
