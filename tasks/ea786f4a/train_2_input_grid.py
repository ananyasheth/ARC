from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
            Background((7,7)),
            Rectangle(((0,0),(6,6)), SolidFill(3)),
            Dot((3,3),SolidFill(0))
			]))

