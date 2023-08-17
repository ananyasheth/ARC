from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,14)),
			Rectangle(((7,0),(8,13)),SolidFill(5)),
			Dot((3,3),SolidFill(1)),
            Dot((1,7),SolidFill(1)),
            Dot((3,7),SolidFill(1)),
            Dot((5,8),SolidFill(1)),
            Dot((3,12),SolidFill(1)),
            Dot((9,1),SolidFill(1)),
            Dot((11,3),SolidFill(1)),
            Dot((11,8),SolidFill(1)),
            Dot((10,11),SolidFill(1)),
			]))