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
                        Dot((0,0),SolidFill(3)),
	                Dot((0,1),SolidFill(3)),
		        Dot((1,9),SolidFill(3)),
		        Dot((5,1),SolidFill(3)),
			Dot((5,5),SolidFill(3)),
			Dot((6,4),SolidFill(3)),
			Dot((9,1),SolidFill(3)),
			Dot((9,4),SolidFill(3)),
			Dot((9,8),SolidFill(3)),
			Dot((9,9),SolidFill(3)),
			Dot((10,10),SolidFill(3))
			]))

