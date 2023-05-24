from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,12)),
            Line(((6,0),(6,11)),SolidFill(3)),
			Line(((0,8),(11,8)),SolidFill(5))
			]))
