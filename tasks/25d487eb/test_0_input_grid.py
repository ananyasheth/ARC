from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((16,11)),
            Triangle(((14,1),(14,7),(11,4)),SolidFill(4)),
            Dot((14,4),SolidFill(8)),
			]))
