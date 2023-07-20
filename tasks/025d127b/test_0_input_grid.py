from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Polyline(((1,1),(1,6),(4,9),(5,9),(5,4),(2,1)),SolidFill(4))       
			]))
