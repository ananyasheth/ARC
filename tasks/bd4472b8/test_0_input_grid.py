from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,5)),
			Dot((0,0),SolidFill(1)),
			Dot((0,1),SolidFill(2)),
            Dot((0,2),SolidFill(3)),
            Dot((0,3),SolidFill(4)),
            Dot((0,4),SolidFill(8)),
			Line(((1,0),(1,4)),SolidFill(5)),
			]))
