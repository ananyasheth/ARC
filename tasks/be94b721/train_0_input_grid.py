from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,13)),
			Polyline(((1,1),(1,2),(2,2),(3,3),(4,3),(4,1),(3,2)),SolidFill(2)),
            Polyline(((1,5),(1,6),(2,6)),SolidFill(3)),
            Polyline(((2,9),(3,8),(4,8),(4,10),(3,9)),SolidFill(1))
			]))
