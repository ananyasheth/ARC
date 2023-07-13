from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Polyline(((4,6),(2,6),(2,2),(7,2),(7,6),(6,6)),SolidFill(5))
            ]))
