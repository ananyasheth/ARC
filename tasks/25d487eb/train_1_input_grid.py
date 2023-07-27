from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,12)),
            Triangle(((8,3),(8,9),(5,6)),SolidFill(8)),
            Dot((8,6),SolidFill(3)),
			]))
