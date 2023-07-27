from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,12)),
            Triangle(((2,2),(2,6),(4,4)),SolidFill(3)),
            Dot((2,4),SolidFill(2)),
			]))
