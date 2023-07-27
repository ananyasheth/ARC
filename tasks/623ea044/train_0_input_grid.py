from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
			Dot((3,3),SolidFill(2)), 
			]))
