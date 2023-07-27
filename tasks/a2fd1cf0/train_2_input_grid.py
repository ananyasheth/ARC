from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,14)),
            Dot((1,11),SolidFill(2)),
            Dot((10,4),SolidFill(3)),
			]))
