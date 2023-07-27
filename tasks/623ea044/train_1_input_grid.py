from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
			Dot((5,11),SolidFill(7)), 
			]))