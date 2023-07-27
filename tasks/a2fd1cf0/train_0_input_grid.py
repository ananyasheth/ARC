from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Dot((1,4),SolidFill(2)),
            Dot((13,10),SolidFill(3)),
			]))
