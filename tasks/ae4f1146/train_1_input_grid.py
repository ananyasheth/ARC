from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Rectangle(((0,1),(2,3)),SolidFill(8)),
                Dot((0,3),SolidFill(1)),
                Dot((1,2),SolidFill(1))
                ]),
            GroupOfShapes([
                Rectangle(((1,5),(3,7)),SolidFill(8)),
                Dot((1,6),SolidFill(1)),
                Dot((2,5),SolidFill(1)),
                Dot((3,7),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((4,2),(6,4)),SolidFill(8)),
                Dot((4,3),SolidFill(1)),
                Dot((5,3),SolidFill(1)),
                Dot((5,2),SolidFill(1)),
                Dot((6,4),SolidFill(1))
                ]),
            GroupOfShapes([
                Rectangle(((6,6),(8,8)),SolidFill(8)),
                Dot((8,6),SolidFill(1)),
                ]),
			]))
