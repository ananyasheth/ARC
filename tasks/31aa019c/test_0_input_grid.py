from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Dot((0,4),SolidFill(2)),
            Dot((0,5),SolidFill(5)),
            Dot((0,6),SolidFill(7)),
            Dot((1,3),SolidFill(5)),
            Dot((1,4),SolidFill(6)),
            Dot((1,6),SolidFill(2)),
            Dot((2,6),SolidFill(3)),
            Dot((3,2),SolidFill(8)),
            Dot((3,4),SolidFill(3)),
            Dot((3,9),SolidFill(8)),
            Dot((4,0),SolidFill(7)),
            Dot((4,1),SolidFill(4)),
            Dot((4,2),SolidFill(7)),
            Dot((4,3),SolidFill(7)),
            Dot((4,4),SolidFill(4)),
            Dot((4,9),SolidFill(4)),
            Dot((5,3),SolidFill(8)),
            Dot((5,6),SolidFill(7)),
            Dot((6,5),SolidFill(9)),
            Dot((6,7),SolidFill(4)),
            Dot((7,0),SolidFill(5)),
            Dot((7,1),SolidFill(5)),
            Dot((7,3),SolidFill(3)),
            Dot((7,6),SolidFill(6)),
            Dot((7,7),SolidFill(7)),
            Dot((7,9),SolidFill(7)),
            Dot((8,2),SolidFill(3)),
            Dot((8,9),SolidFill(2)),
            Dot((9,0),SolidFill(1)),
            Dot((9,2),SolidFill(1)),
            Dot((9,8),SolidFill(6)),
            Dot((9,9),SolidFill(7)),
			]))
