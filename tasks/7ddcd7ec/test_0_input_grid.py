from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Rectangle(((4,3),(5,4)),SolidFill(8)),
			Dot((6,2),SolidFill(8)),
            Dot((6,5),SolidFill(8)),
            Dot((3,5),SolidFill(8))
			]))