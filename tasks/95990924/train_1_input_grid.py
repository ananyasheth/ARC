from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
            Rectangle(((2,2),(3,3)),SolidFill(5)),
            Rectangle(((6,6),(7,7)),SolidFill(5)),
			]))
