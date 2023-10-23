from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,8)),
            GroupOfShapes([
                Dot((1,0),SolidFill(2)),
                Dot((1,1),SolidFill(2)),
                Dot((1,2),SolidFill(1)),
                Dot((1,3),SolidFill(2)),
                Dot((1,4),SolidFill(1)),
                Dot((1,5),SolidFill(2)),
                Dot((1,6),SolidFill(1)),
                Dot((1,7),SolidFill(1)),
            ]),
            GroupOfShapes([
                Dot((3,0),SolidFill(3)),
                Dot((3,1),SolidFill(3)),
                Dot((3,2),SolidFill(1)),
            ]),
            GroupOfShapes([
                Dot((7,0),SolidFill(8)),
                Dot((7,1),SolidFill(8)),
                Dot((7,2),SolidFill(2)),
            ])
			]))
