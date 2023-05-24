from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,3)),
			Dot((0,0),SolidFill(5)),
		    Dot((1,1),SolidFill(5)),
            Dot((2,0),SolidFill(5))
			]))

