from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((2,0),SolidFill(2)),
            Dot((0,2),SolidFill(2)),
            Dot((5,3),SolidFill(4)),
            Dot((9,7),SolidFill(4)),
            Dot((0,5),SolidFill(6)),
            Dot((4,9),SolidFill(6)),
			]))
