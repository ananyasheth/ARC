from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Rectangle(((2,4),(3,5)),SolidFill(4)),
			Dot((1,6),SolidFill(4)),
            Dot((4,6),SolidFill(4))
			]))