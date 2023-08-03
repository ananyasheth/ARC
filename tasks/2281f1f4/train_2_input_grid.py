from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		Dot((0,2),SolidFill(5)),
        Dot((0,3),SolidFill(5)),
        Dot((0,5),SolidFill(5)),
        Dot((0,7),SolidFill(5)),
        Dot((0,8),SolidFill(5)),
        Dot((2,9),SolidFill(5)),
        Dot((3,9),SolidFill(5)),
        Dot((6,9),SolidFill(5)),
        Dot((8,9),SolidFill(5)),
		]))
