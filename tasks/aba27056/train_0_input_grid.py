from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,7)),
			Polyline(((4,2),(4,1),(6,1),(6,5),(4,5),(4,4)),SolidFill(6)),
			]))
