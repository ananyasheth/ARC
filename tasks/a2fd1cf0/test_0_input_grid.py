from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,14)),
            Dot((2,1),SolidFill(2)),
            Dot((10,10),SolidFill(3)),
			]))
