from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return GroupOfShapes([
			Background((9,9)),
				Polyline(((1,0),(2,0),(2,1),(3,1)),SolidFill(4)),
				Polyline(((7,1),(8,1),(8,2),(7,3),(7,2)),SolidFill(5)),
				Polyline(((5,3),(2,3),(2,5),(3,4),(3,5),(5,5)),SolidFill(3)),
				Polyline(((7,6),(8,6),(8,7),(6,7),(6,8),(7,8)),SolidFill(6))
			])