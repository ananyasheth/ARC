from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((5,5)),
		Line(((4,0),(4,4)),SolidFill(5)),
		Dot((3,2),SolidFill(5)),
        Dot((2,2),SolidFill(1)),
		]))
