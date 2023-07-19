from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,6)),
			Polyline(((3,1),(3,0),(0,0),(0,5),(3,5),(3,4)),SolidFill(3)),
			]))
