from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((8,0),(14,3)),SolidFill(2)),
            Rectangle(((9,5),(14,7)),SolidFill(4)),
            Rectangle(((12,10),(14,14)),SolidFill(1)),
			]))
