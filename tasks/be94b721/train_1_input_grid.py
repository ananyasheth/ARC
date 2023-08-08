from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((5,10)),
			Polyline(((2,0),(1,1),(2,1),(2,2),(3,1)),SolidFill(3)),
            Polyline(((1,4),(1,5),(3,5),(3,4),(2,4)),SolidFill(4)), 
            Polyline(((0,7),(0,8),(1,8)),SolidFill(6))
			]))