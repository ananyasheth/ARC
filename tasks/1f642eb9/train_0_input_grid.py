from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Rectangle(((3,4),(6,5)),SolidFill(8)),
            Dot((0,4),SolidFill(9)),
            Dot((6,0),SolidFill(6)),
            Dot((9,5),SolidFill(4))
			]))

