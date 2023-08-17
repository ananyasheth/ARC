from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,7)),
            Line(((0,1),(0,2)),SolidFill(2)),
            Line(((1,4),(1,4)),SolidFill(3)),
            Line(((2,0),(2,2)),SolidFill(1)),
            Line(((4,1),(4,6)),SolidFill(5)),
            Line(((6,0),(6,4)),SolidFill(6)),
            Line(((7,3),(7,6)),SolidFill(4)),
			Line(((9,0),(9,6)),SolidFill(8)),
			]))


