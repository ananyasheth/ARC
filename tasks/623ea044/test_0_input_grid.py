from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((17,17)),
			Dot((7,12),SolidFill(6)), 
			]))