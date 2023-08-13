from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((12,11)),
		Rectangle(((1,1),(4,4)),SolidFill(2)),
        Rectangle(((7,2),(9,7)),SolidFill(1)),
		]))
