from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,6)),
			Line(((0,1),(1,1)),SolidFill(8)),
			Line(((3,4),(3,5)),SolidFill(2))
			]))
