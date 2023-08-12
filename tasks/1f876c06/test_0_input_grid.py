from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((1,0),SolidFill(7)),
            Dot((7,6),SolidFill(7)),
            Dot((4,0),SolidFill(6)),
            Dot((7,3),SolidFill(6)),
            Dot((3,3),SolidFill(3)),
            Dot((0,6),SolidFill(3)),
            Dot((0,9),SolidFill(9)),
            Dot((3,6),SolidFill(9)),
            Dot((9,5),SolidFill(4)),
            Dot((5,9),SolidFill(4)),
			]))
