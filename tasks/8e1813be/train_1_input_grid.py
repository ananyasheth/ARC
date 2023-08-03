from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,10)),
            Line(((0,2),(11,2)),SolidFill(1)),
            Line(((0,5),(11,5)),SolidFill(2)),
            Line(((0,8),(11,8)),SolidFill(4)),
            Rectangle(((1,1),(3,3)),SolidFill(5)),
            RectangleOutline(((0,0),(4,4)),SolidFill(0))
			]))
