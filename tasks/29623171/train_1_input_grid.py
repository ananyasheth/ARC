from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,9)),
			Line(((3,0),(3,2)),SolidFill(2))
			]))
