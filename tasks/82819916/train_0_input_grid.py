from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,8)),
            GroupOfShapes([
                Dot((1,0),SolidFill(3)),
                Dot((1,1),SolidFill(3)),
                Dot((1,2),SolidFill(2)),
                Dot((1,3),SolidFill(3)),
                Dot((1,4),SolidFill(3)),
                Dot((1,5),SolidFill(2)),
                Dot((1,6),SolidFill(3)),
                Dot((1,7),SolidFill(3)),
            ]),
            GroupOfShapes([
                Dot((4,0),SolidFill(8)),
                Dot((4,1),SolidFill(8)),
                Dot((4,2),SolidFill(4)),
            ]),
            GroupOfShapes([
                Dot((6,0),SolidFill(1)),
                Dot((6,1),SolidFill(1)),
                Dot((6,2),SolidFill(6)),
            ])
			]))
