from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,8)),
			Dot((1,1),SolidFill(3)),
            Dot((4,2),SolidFill(3)),
            Dot((4,4),SolidFill(7)),
            Dot((3,7),SolidFill(7))
			]))

