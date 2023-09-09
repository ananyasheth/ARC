from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
			GroupOfShapes([
				Dot((3,5),SolidFill(7)),
				Dot((4,5),SolidFill(7)),
				Dot((4,4),SolidFill(7)),
				Dot((5,3),SolidFill(7)),
			])

			]))
