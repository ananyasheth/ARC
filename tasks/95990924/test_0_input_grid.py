from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((1,1),(2,2)),SolidFill(5)),
            Rectangle(((4,5),(5,6)),SolidFill(5)),
            Rectangle(((1,11),(2,12)),SolidFill(5)),
            Rectangle(((10,2),(11,3)),SolidFill(5)),
            Rectangle(((11,9),(12,10)),SolidFill(5)),
            Rectangle(((6,12),(7,13)),SolidFill(5)),
			]))
