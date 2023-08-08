from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((11,13)),
			RectangleOutline(((2,2),(8,8)),SolidFill(1)),
            Line(((2,4),(8,4)),SolidFill(1)),
            Dot((4,2),SolidFill(0)),
            Dot((7,2),SolidFill(0)),
            Line(((2,5),(2,6)),SolidFill(0)),
            Dot((8,6),SolidFill(0)),
            Dot((8,8),SolidFill(0)),
            Dot((4,8),SolidFill(0)),
            Dot((3,4),SolidFill(0)),
            Dot((6,4),SolidFill(0))
			]))
