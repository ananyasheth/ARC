from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Rectangle(((0,2),(2,4)),SolidFill(8)),
                Dot((0,2),SolidFill(1)),
                Dot((0,3),SolidFill(1)),
                Dot((2,2),SolidFill(1)),
                Dot((2,3),SolidFill(1)),
                Dot((1,4),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((1,6),(3,8)),SolidFill(8)),
                Dot((1,7),SolidFill(1)),
                Dot((1,8),SolidFill(1)),
                Dot((2,6),SolidFill(1)),
                Dot((2,7),SolidFill(1)),
                Dot((2,8),SolidFill(1)),
                Dot((3,7),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((4,0),(6,2)),SolidFill(8)),
                Dot((5,2),SolidFill(1)),
                Dot((6,0),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((5,4),(7,6)),SolidFill(8)),
                Dot((5,5),SolidFill(1)),
                Dot((6,4),SolidFill(1)),
                Dot((7,6),SolidFill(1)),
                ]),
			]))
