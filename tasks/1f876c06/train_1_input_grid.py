from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((0,0),SolidFill(9)),
            Dot((3,3),SolidFill(9)),
            Dot((7,1),SolidFill(8)),
            Dot((2,6),SolidFill(8)),
            Dot((5,5),SolidFill(7)),
            Dot((9,9),SolidFill(7)),
            Dot((0,7),SolidFill(3)),
            Dot((2,9),SolidFill(3)),
			]))
