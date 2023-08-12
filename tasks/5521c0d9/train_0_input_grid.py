from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((11,1),(14,2)),SolidFill(1)),
            Rectangle(((13,4),(14,7)),SolidFill(2)),
            Rectangle(((11,9),(14,12)),SolidFill(4)),
			]))
