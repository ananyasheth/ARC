from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,4)),
			Dot((0,0),SolidFill(3)),
			Dot((0,1),SolidFill(2)),
			Dot((0,2),SolidFill(1)),
            Dot((0,3),SolidFill(4)),
			Line(((1,0),(1,3)),SolidFill(5)),
			]))
