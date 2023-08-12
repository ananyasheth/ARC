from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,6)),
            Line(((0,0),(0,5)),SolidFill(3)),
            Line(((1,0),(1,5)),SolidFill(5)),
            Line(((2,0),(2,5)),SolidFill(5)),
			]))