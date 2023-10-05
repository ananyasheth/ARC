from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,5)),
            Dot((1,4),SolidFill(2)),
			]))
