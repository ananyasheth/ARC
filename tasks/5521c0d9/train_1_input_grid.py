from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((9,1),(14,4)),SolidFill(4)),
            Rectangle(((13,7),(14,8)),SolidFill(1)),
            Rectangle(((10,11),(14,12)),SolidFill(2)),
			]))
