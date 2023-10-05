from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,3)),
            Dot((0,0),SolidFill(7)),
            Dot((0,1),SolidFill(7)),
            Dot((1,1),SolidFill(7)),
            Dot((2,2),SolidFill(7)),
			]))


