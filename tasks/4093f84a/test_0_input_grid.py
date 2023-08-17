from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,14)),
			Rectangle(((0,5),(13,6)),SolidFill(5)),
			Dot((1,2),SolidFill(4)),
            Dot((3,3),SolidFill(4)),
            Dot((4,1),SolidFill(4)),
            Dot((11,1),SolidFill(4)),
            Dot((11,3),SolidFill(4)),
            Dot((1,9),SolidFill(4)),
            Dot((6,7),SolidFill(4)),
            Dot((6,11),SolidFill(4)),
            Dot((11,10),SolidFill(4)),
            Dot((13,12),SolidFill(4)),
			]))