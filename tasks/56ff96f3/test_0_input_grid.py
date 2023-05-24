from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,8)),
			Dot((0,0),SolidFill(8)),
			Dot((1,2),SolidFill(8)),
            Dot((4,5),SolidFill(6)),
            Dot((7,1),SolidFill(6))
			]))
