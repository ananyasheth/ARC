from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,8)),
            GroupOfShapes([
                Dot((1,0),SolidFill(1)),
                Dot((1,1),SolidFill(4)),
                Dot((1,2),SolidFill(1)),
                Dot((1,3),SolidFill(4)),
                Dot((1,4),SolidFill(4)),
                Dot((1,5),SolidFill(1)),
                Dot((1,6),SolidFill(4)),
                Dot((1,7),SolidFill(1)),
            ]),
            GroupOfShapes([
                Dot((4,0),SolidFill(2)),
                Dot((4,1),SolidFill(3)),
            ]),
            GroupOfShapes([
                Dot((6,0),SolidFill(8)),
                Dot((6,1),SolidFill(2)),
            ]),
            GroupOfShapes([
                Dot((8,0),SolidFill(6)),
                Dot((8,1),SolidFill(5)),
            ])            
			]))
