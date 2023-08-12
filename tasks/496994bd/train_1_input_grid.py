from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,5)),
            Line(((0,0),(0,4)),SolidFill(2)),
            Line(((1,0),(1,4)),SolidFill(8)),
			]))