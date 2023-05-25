from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((11,11)),
			Line(((0,3),(10,3)),SolidFill(5)),
                        Line(((0,7),(10,7)),SolidFill(5)),
                        Line(((3,0),(3,10)),SolidFill(5)),
                        Line(((7,0),(7,10)),SolidFill(5)),
                        Dot((0,0),SolidFill(4)),
	                Dot((0,1),SolidFill(4)),
		        Dot((1,1),SolidFill(4)),
			Dot((2,0),SolidFill(4)),
			Dot((1,6),SolidFill(4)),
			Dot((1,8),SolidFill(4)),
			Dot((1,9),SolidFill(4)),
			Dot((2,9),SolidFill(4)),
			Dot((5,0),SolidFill(4)),
			Dot((5,5),SolidFill(4)),
			Dot((5,8),SolidFill(4)),
	                Dot((5,10),SolidFill(4)),
		        Dot((4,9),SolidFill(4)),
		        Dot((9,0),SolidFill(4)),
			Dot((9,6),SolidFill(4)),
			Dot((8,5),SolidFill(4)),
			Dot((10,4),SolidFill(4)),
			Dot((10,5),SolidFill(4)),
			Dot((8,10),SolidFill(4)),
			Dot((9,9),SolidFill(4))
			]))

