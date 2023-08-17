from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,14)),
			Rectangle(((5,0),(8,13)),SolidFill(5)),
			Dot((2,2),SolidFill(2)),
            Dot((0,8),SolidFill(2)),
            Dot((3,10),SolidFill(2)),
            Dot((10,1),SolidFill(2)),
            Dot((11,4),SolidFill(2)),
            Dot((9,9),SolidFill(2)),
            Dot((12,11),SolidFill(2)),
			]))