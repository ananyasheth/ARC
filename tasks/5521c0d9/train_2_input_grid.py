from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((14,1),(14,4)),SolidFill(2)),
            Rectangle(((11,7),(14,7)),SolidFill(1)),
            Rectangle(((12,11),(14,12)),SolidFill(4)),
			]))
