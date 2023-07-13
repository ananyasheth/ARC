from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Polyline(((7,4),(7,2),(2,2),(2,7),(7,7),(7,6)),SolidFill(5))
            ]))
