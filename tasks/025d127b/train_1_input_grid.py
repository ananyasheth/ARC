from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,9)),
			Polyline(((1,1),(1,5),(4,8),(5,8),(5,4),(2,1)),SolidFill(8))
			]))
