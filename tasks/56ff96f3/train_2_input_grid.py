from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((2,1),SolidFill(4)),
		    Dot((6,5),SolidFill(4))
			]))

