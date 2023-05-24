from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,4)),
			Line(((0,1),(3,1)),SolidFill(3)),
			Line(((1,0),(1,3)),SolidFill(2))
			]))
