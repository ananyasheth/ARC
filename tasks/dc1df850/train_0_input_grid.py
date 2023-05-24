from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((5,5)),
			Dot((0,0),SolidFill(2)),
            Dot((1,3),SolidFill(2)),
            Dot((3,1),SolidFill(6))
			]))

