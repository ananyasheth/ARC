from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Polyline(((5,4),(5,2),(9,2),(9,7),(5,7),(5,6)),SolidFill(5))
            ]))