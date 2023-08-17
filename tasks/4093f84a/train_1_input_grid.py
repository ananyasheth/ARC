from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,14)),
			Rectangle(((0,4),(13,8)),SolidFill(5)),
			Dot((4,0),SolidFill(3)),
            Dot((2,3),SolidFill(3)),
            Dot((7,1),SolidFill(3)),
            Dot((9,2),SolidFill(3)),
            Dot((0,12),SolidFill(3)),
            Dot((1,9),SolidFill(3)),
            Dot((2,11),SolidFill(3)),
            Dot((6,10),SolidFill(3)),
            Dot((6,12),SolidFill(3)),
            Dot((9,12),SolidFill(3)),
            Dot((12,10),SolidFill(3)),
			]))