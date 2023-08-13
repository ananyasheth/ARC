from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((13,15)),
		Rectangle(((1,2),(6,6)),SolidFill(2)),
		Rectangle(((1,10),(3,12)),SolidFill(1)),
        Rectangle(((8,8),(12,14)),SolidFill(3)),
		]))
