from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,4)),
            Line(((0,3),(0,3)),SolidFill(1)),
            Line(((2,0),(2,2)),SolidFill(2)),
            Line(((4,1),(4,2)),SolidFill(3)),
            Line(((6,0),(6,3)),SolidFill(8)),
			]))

