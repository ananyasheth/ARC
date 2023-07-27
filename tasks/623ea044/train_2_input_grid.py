from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,7)),
			Dot((3,2),SolidFill(8)), 
			]))