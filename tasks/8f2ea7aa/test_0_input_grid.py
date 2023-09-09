from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Dot((3,0),SolidFill(2)),
                Dot((4,0),SolidFill(2)),
                Dot((4,1),SolidFill(2)),
                Dot((5,1),SolidFill(2)),
                Dot((5,2),SolidFill(2)),
            ])

			]))
