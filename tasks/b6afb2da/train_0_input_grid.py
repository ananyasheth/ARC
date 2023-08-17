from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Rectangle(((2,1),(5,4)),SolidFill(5)),
            Rectangle(((5,6),(9,9)),SolidFill(5)),
			]))


