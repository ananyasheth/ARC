from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((11,8)),
            Line(((0,0),(0,2)),SolidFill(6)),
            Line(((1,4),(1,7)),SolidFill(1)),
            Line(((3,1),(3,5)),SolidFill(4)),
            Line(((4,5),(4,6)),SolidFill(7)),
            Line(((6,0),(6,6)),SolidFill(2)),
            Line(((7,2),(7,7)),SolidFill(3)),
            Line(((8,1),(8,1)),SolidFill(9)),
			Line(((10,0),(10,7)),SolidFill(8)),
			]))


