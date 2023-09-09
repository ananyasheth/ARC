from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Dot((0,4),SolidFill(6)),
                Dot((1,3),SolidFill(6)),
                Dot((1,5),SolidFill(6)),
                Dot((2,3),SolidFill(6)),
                Dot((2,4),SolidFill(6)),
            ])

			]))
