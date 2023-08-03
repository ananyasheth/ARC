from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,2)),
			Dot((0,0),SolidFill(8)),
			Dot((0,1),SolidFill(3)),
			Line(((1,0),(1,1)),SolidFill(5)),
			]))
