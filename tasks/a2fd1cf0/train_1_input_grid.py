from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,16)),
            Dot((7,1),SolidFill(2)),
            Dot((1,11),SolidFill(3)),
			]))
