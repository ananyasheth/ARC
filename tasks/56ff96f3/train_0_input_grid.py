from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((1,6),SolidFill(1)),
            Dot((3,1),SolidFill(1)),
            Dot((5,3),SolidFill(2)),
            Dot((7,7),SolidFill(2))
			]))

