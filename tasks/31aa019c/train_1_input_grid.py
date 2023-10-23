from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((0,0),SolidFill(2)),
            Dot((0,1),SolidFill(7)),
            Dot((0,2),SolidFill(7)),
            Dot((0,3),SolidFill(1)),
            Dot((0,5),SolidFill(3)),
            Dot((0,9),SolidFill(3)),
            Dot((1,3),SolidFill(9)),
            Dot((1,8),SolidFill(3)),
            Dot((1,9),SolidFill(7)),
            Dot((2,3),SolidFill(1)),
            Dot((2,7),SolidFill(6)),
            Dot((2,9),SolidFill(9)),
            Dot((3,7),SolidFill(1)),
            Dot((4,0),SolidFill(9)),
            Dot((5,4),SolidFill(2)),
            Dot((5,8),SolidFill(3)),
            Dot((6,1),SolidFill(5)),
            Dot((6,3),SolidFill(7)),
            Dot((6,4),SolidFill(3)),
            Dot((6,8),SolidFill(1)),
            Dot((7,0),SolidFill(4)),
            Dot((7,1),SolidFill(4)),
            Dot((7,5),SolidFill(1)),
            Dot((7,9),SolidFill(5)),
            Dot((8,7),SolidFill(5)),
            Dot((8,8),SolidFill(3)),
            Dot((9,4),SolidFill(4)),
            Dot((9,5),SolidFill(5)),
			]))
