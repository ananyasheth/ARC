from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((18,15)),
            Line(((2,0),(2,14)),SolidFill(2)),
            Line(((5,0),(5,14)),SolidFill(1)),
            Line(((8,0),(8,14)),SolidFill(3)),
            Line(((11,0),(11,14)),SolidFill(4)),
            Line(((14,0),(14,14)),SolidFill(8)),
            Line(((17,0),(17,14)),SolidFill(6)),
            Rectangle(((10,1),(15,6)),SolidFill(5)),
            RectangleOutline(((9,0),(16,7)),SolidFill(0))
			]))

