from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,8)),
			Line(((4,0),(4,7)),SolidFill(8)),
			Line(((0,4),(7,4)),SolidFill(6))
			]))
