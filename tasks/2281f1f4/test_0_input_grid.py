from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		Dot((0,0),SolidFill(5)),
        Dot((0,2),SolidFill(5)),
        Dot((0,3),SolidFill(5)),
        Dot((0,6),SolidFill(5)),
        Dot((0,8),SolidFill(5)),
        Dot((2,9),SolidFill(5)),
        Dot((3,9),SolidFill(5)),
        Dot((5,9),SolidFill(5)),
        Dot((7,9),SolidFill(5)),
        Dot((9,9),SolidFill(5)),
		]))
