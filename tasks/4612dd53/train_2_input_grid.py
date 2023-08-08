from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((13,13)),
			RectangleOutline(((3,2),(10,10)),SolidFill(1)),
            Line(((7,2),(7,10)),SolidFill(1)),
            Dot((5,2),SolidFill(0)),
            Dot((9,2),SolidFill(0)),
            Dot((3,4),SolidFill(0)),
            Dot((3,7),SolidFill(0)),
            Dot((10,4),SolidFill(0)),
            Line(((10,7),(10,8)),SolidFill(0)),
            Dot((5,10),SolidFill(0)),
            Dot((7,10),SolidFill(0)),
            Dot((7,4),SolidFill(0)),
            Dot((7,6),SolidFill(0)),
            Dot((7,9),SolidFill(0))
			]))
