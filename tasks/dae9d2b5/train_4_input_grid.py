from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,6)),
			Dot((1,0),SolidFill(4)),
			Dot((2,2),SolidFill(4)),
            Dot((2,3),SolidFill(3)),
            Dot((0,4),SolidFill(3)),
            Dot((2,4),SolidFill(3))
			]))

