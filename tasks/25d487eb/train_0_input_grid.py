from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,15)),
            Triangle(((2,3),(6,3),(4,5)),SolidFill(2)),
            Dot((4,3),SolidFill(1)),
			]))
