from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
            Background((5,5)),
            Rectangle(((0,0),(4,4)), SolidFill(2)),
            Dot((2,2),SolidFill(0))
			]))

