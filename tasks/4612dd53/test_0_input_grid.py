from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((13,13)),
			RectangleOutline(((2,2),(10,10)),SolidFill(1)),
            Line(((7,2),(7,10)),SolidFill(1)),
            Line(((4,2),(5,2)),SolidFill(0)),
            Dot((8,2),SolidFill(0)),
            Dot((2,3),SolidFill(0)),
            Dot((2,6),SolidFill(0)),
            Dot((2,8),SolidFill(0)),
            Dot((10,3),SolidFill(0)),
            Dot((10,6),SolidFill(0)),
            Dot((10,8),SolidFill(0)),
            Line(((4,10),(5,10)),SolidFill(0)),
            Dot((8,10),SolidFill(0)),
            Dot((7,3),SolidFill(0)),
            Dot((7,5),SolidFill(0)),
            Line(((7,7),(7,8)),SolidFill(0))            
			]))
