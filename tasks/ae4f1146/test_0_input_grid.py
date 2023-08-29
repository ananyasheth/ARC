from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
            GroupOfShapes([
                Rectangle(((0,0),(2,2)),SolidFill(8)),
                Dot((2,0),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((3,3),(5,5)),SolidFill(8)),
                Dot((3,4),SolidFill(1)),
                Dot((4,5),SolidFill(1)),
                Dot((5,3),SolidFill(1)),
                ]),
            GroupOfShapes([
                Rectangle(((0,6),(2,8)),SolidFill(8)),
                Dot((0,7),SolidFill(1)),
                Dot((1,6),SolidFill(1)),
                Dot((1,8),SolidFill(1)),
                Dot((2,7),SolidFill(1))
                ]),
            GroupOfShapes([
                Rectangle(((6,6),(8,8)),SolidFill(8)),
                Dot((6,6),SolidFill(1)),
                Dot((6,7),SolidFill(1)),
                Dot((7,7),SolidFill(1)),
                Dot((7,8),SolidFill(1)),
                Dot((8,7),SolidFill(1)),
                Dot((8,6),SolidFill(1)),
                ]),
			]))
