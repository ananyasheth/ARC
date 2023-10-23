from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
			Dot((4,1),SolidFill(5)),
            Dot((7,1),SolidFill(5)),
            Dot((1,7),SolidFill(5)),
            Dot((4,7),SolidFill(5)),
			]))
