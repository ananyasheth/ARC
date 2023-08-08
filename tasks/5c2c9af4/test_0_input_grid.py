from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((28,28)),
		Dot((12,7),SolidFill(4)),
		Dot((18,13),SolidFill(4)),
		Dot((24,19),SolidFill(4)),
		]))
