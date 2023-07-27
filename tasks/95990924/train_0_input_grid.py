from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
            Rectangle(((3,4),(4,5)),SolidFill(5)),
			]))
