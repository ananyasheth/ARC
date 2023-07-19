from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Polyline(((1,4),(0,4),(0,1),(8,1),(8,4),(7,4)),SolidFill(2)),
			]))
