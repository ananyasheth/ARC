from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((2,0),SolidFill(2)),
            Dot((0,3),SolidFill(1)),
            Dot((2,5),SolidFill(2)),
            Dot((0,7),SolidFill(5)),
            Dot((2,9),SolidFill(1)),
            Dot((3,2),SolidFill(1)),
            Dot((3,9),SolidFill(5)),
            Dot((4,2),SolidFill(8)),
            Dot((6,1),SolidFill(4)),
            Dot((7,1),SolidFill(5)),
            Dot((7,2),SolidFill(1)),
            Dot((7,4),SolidFill(1)),
            Dot((8,1),SolidFill(8)),
            Dot((8,2),SolidFill(1)),
            Dot((8,6),SolidFill(1)),
            Dot((8,8),SolidFill(3)),
            Dot((9,7),SolidFill(3)),
			]))
