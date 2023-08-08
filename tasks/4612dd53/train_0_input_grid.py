from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,13)),
			RectangleOutline(((1,2),(7,10)),SolidFill(1)),
            Line(((3,2),(5,2)),SolidFill(0)),
            Dot((1,3),SolidFill(0)),
            Line(((1,5),(1,6)),SolidFill(0)),
            Dot((1,9),SolidFill(0)),
            Line(((7,4),(7,5)),SolidFill(0)),
            Dot((7,8),SolidFill(0)),
            Dot((2,10),SolidFill(0)),
            Dot((4,10),SolidFill(0))
			]))
