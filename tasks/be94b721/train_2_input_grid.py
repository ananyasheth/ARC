from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,11)),
			Polyline(((1,1),(1,3),(2,2),(4,2),(4,1),(3,1)),SolidFill(8)),
            Polyline(((3,5),(2,6),(4,6)),SolidFill(2)),
            Polyline(((1,8),(1,9),(4,9)),SolidFill(7))
			]))