from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
			Dot((1,4),SolidFill(5)),
            Dot((4,4),SolidFill(5)),
            Dot((7,4),SolidFill(5)),
            Dot((7,7),SolidFill(5)),
			]))
