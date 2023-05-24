from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,11)),
			Dot((1,1),SolidFill(7)),
			Dot((3,7),SolidFill(7))
			]))

