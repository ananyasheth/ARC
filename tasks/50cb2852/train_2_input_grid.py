from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((12,13)),
		Rectangle(((2,0),(5,3)),SolidFill(3)),
        Rectangle(((1,6),(6,9)),SolidFill(2)),
        Rectangle(((8,2),(11,9)),SolidFill(1)),
		]))
