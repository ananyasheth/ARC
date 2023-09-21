from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,14)),
            GroupOfShapes([
                Rectangle(((0,0),(3,3)),SolidFill(5))
            ]),
            GroupOfShapes([
                Rectangle(((0,5),(3,8)),SolidFill(5)),
                Rectangle(((2,6),(3,7)),SolidFill(0)),
            ]),
            GroupOfShapes([
                Rectangle(((0,10),(3,13)),SolidFill(5))
            ]),
			]))