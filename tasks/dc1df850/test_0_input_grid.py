from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((1,2),SolidFill(2)),
            Dot((3,7),SolidFill(2)),
            Dot((7,5),SolidFill(2)),
            Dot((0,8),SolidFill(7)),
            Dot((5,1),SolidFill(7)),
            Dot((9,9),SolidFill(5))
			]))

