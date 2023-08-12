from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
            Background((11,11)),
            Rectangle(((0,0),(10,10)), SolidFill(6)),
            Dot((5,5),SolidFill(0))
			]))

