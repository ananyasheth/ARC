from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((0,0),SolidFill(6)),
            Dot((0,4),SolidFill(8)),
            Dot((1,8),SolidFill(2)),
            Dot((1,9),SolidFill(8)),
            Dot((2,1),SolidFill(7)),
            Dot((2,4),SolidFill(2)),
            Dot((2,6),SolidFill(5)),
            Dot((2,8),SolidFill(2)),
            Dot((3,1),SolidFill(9)),
            Dot((3,3),SolidFill(1)),
            Dot((4,1),SolidFill(9)),
            Dot((4,9),SolidFill(1)),
            Dot((5,5),SolidFill(6)),
            Dot((6,1),SolidFill(1)),
            Dot((6,3),SolidFill(7)),
            Dot((8,6),SolidFill(3)),
            Dot((9,2),SolidFill(5)),
			]))
