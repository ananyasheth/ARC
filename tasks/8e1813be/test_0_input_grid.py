from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((19,19)),
            Line(((0,0),(0,18)),SolidFill(2)),
            Line(((3,0),(3,18)),SolidFill(3)),
            Line(((6,0),(6,18)),SolidFill(8)),
            Line(((9,0),(9,18)),SolidFill(4)),
            Line(((12,0),(12,18)),SolidFill(6)),
            Line(((15,0),(15,18)),SolidFill(1)),
            Line(((18,0),(18,18)),SolidFill(7)),
            Rectangle(((1,8),(7,14)),SolidFill(5)),
            RectangleOutline(((0,7),(8,15)),SolidFill(0))
			]))
