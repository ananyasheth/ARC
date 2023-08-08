from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,9)),
			Polyline(((4,0),(4,2),(5,1)),SolidFill(8)),
            Polyline(((1,3),(2,3),(2,4),(3,4)),SolidFill(7)),
            Polyline(((1,6),(1,8),(3,6),(3,8)),SolidFill(2))
			]))