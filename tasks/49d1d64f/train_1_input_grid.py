from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((2,3)),
		Dot((0,0),SolidFill(1)),
        Dot((0,1),SolidFill(8)),
        Dot((0,2),SolidFill(4)),
        Dot((1,0),SolidFill(8)),
        Dot((1,1),SolidFill(3)),
        Dot((1,2),SolidFill(8)),
		]))
