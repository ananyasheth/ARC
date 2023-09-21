from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,3)),
            GroupOfShapes([
                Dot((0,0),SolidFill(7)),
                Dot((1,0),SolidFill(6)),
                Dot((2,0),SolidFill(6)),                
            ]),
            GroupOfShapes([
                Dot((0,1),SolidFill(6)),
                Dot((1,1),SolidFill(7)),
                Dot((2,1),SolidFill(2)),
            ]),
            GroupOfShapes([
                Dot((0,2),SolidFill(1)),
                Dot((1,2),SolidFill(6)),
                Dot((2,2),SolidFill(2)),
            ])
			]))