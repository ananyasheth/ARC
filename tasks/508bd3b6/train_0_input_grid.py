from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,12)),
			Line(((0,10),(11,10)),SolidFill(2)),
            Line(((0,11),(11,11)),SolidFill(2)),
            Line(((11,2),(10,3)),SolidFill(8))
			]))

