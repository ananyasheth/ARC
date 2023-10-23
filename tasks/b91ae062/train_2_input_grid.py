from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,3)),
			Dot((0,0),SolidFill(3)),
            Dot((0,1),SolidFill(2)),
            Dot((1,1),SolidFill(7)),
            Dot((1,2),SolidFill(3)),
			]))


