from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,9)),
			Polyline(((1,1),(1,3),(4,6),(5,6),(5,4),(2,1)),SolidFill(6)),
			Polyline(((7,2),(7,4),(8,5),(9,5),(9,3),(8,2)),SolidFill(2))     
			]))
