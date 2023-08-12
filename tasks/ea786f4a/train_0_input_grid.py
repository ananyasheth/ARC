from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
            Background((3,3)),
            Rectangle(((0,0),(2,2)), SolidFill(1)),
            Dot((1,1),SolidFill(0))
			]))

