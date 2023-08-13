from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((14,13)),
		Rectangle(((0,1),(3,5)),SolidFill(1)),
        Rectangle(((1,8),(3,10)),SolidFill(1)),
        Rectangle(((5,2),(10,7)),SolidFill(2)),
        Rectangle(((7,9),(13,12)),SolidFill(3)),
		]))
