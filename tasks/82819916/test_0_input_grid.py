from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,10)),
            GroupOfShapes([
                Dot((1,0),SolidFill(2)),
                Dot((1,1),SolidFill(2)),
                Dot((1,2),SolidFill(1)),
                Dot((1,3),SolidFill(2)),
                Dot((1,4),SolidFill(1)),
                Dot((1,5),SolidFill(2)),
                Dot((1,6),SolidFill(1)),
                Dot((1,7),SolidFill(1)),
                Dot((1,8),SolidFill(2)),
                Dot((1,9),SolidFill(1)),
            ]),
            GroupOfShapes([
                Dot((3,0),SolidFill(8)),
                Dot((3,1),SolidFill(8)),
                Dot((3,2),SolidFill(3)),
            ]),
            GroupOfShapes([
                Dot((6,0),SolidFill(1)),
                Dot((6,1),SolidFill(1)),
                Dot((6,2),SolidFill(4)),
            ]),
            GroupOfShapes([
                Dot((9,0),SolidFill(6)),
                Dot((9,1),SolidFill(6)),
                Dot((9,2),SolidFill(8)),
            ]),
            GroupOfShapes([
                Dot((11,0),SolidFill(1)),
                Dot((11,1),SolidFill(1)),
                Dot((11,2),SolidFill(6)),
            ]),
			]))
