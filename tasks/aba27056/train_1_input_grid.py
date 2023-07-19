from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
			Polyline(((3,4),(2,4),(2,8),(8,8),(8,4),(7,4)),SolidFill(7)),
			]))
