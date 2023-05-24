from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,7)),
			Line(((3,0),(3,1)),SolidFill(2))
			]))

