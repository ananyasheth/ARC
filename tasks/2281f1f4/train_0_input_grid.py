from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((10,10)),
		Dot((0,0),SolidFill(5)),
        Dot((0,3),SolidFill(5)),
        Dot((0,7),SolidFill(5)),
        Dot((3,9),SolidFill(5)),
        Dot((7,9),SolidFill(5)),
		]))
