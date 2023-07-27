from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
            Rectangle(((2,3),(3,4)),SolidFill(5)),
            Rectangle(((4,8),(5,9)),SolidFill(5)),
            Rectangle(((8,4),(9,5)),SolidFill(5)),
            Rectangle(((11,9),(12,10)),SolidFill(5)),
			]))
