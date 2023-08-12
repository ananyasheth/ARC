from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((3,0),SolidFill(6)),
            Dot((0,3),SolidFill(6)),
            Dot((2,2),SolidFill(4)),
            Dot((6,6),SolidFill(4)),
            Dot((0,5),SolidFill(8)),
            Dot((4,9),SolidFill(8)),
            Dot((9,0),SolidFill(9)),
            Dot((5,4),SolidFill(9)),
			]))
