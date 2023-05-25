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
                        Dot((1,0),SolidFill(1)),
	                Dot((2,6),SolidFill(1)),
		        Dot((1,9),SolidFill(1)),
		        Dot((4,6),SolidFill(1)),
			Dot((5,9),SolidFill(1)),
			Dot((9,1),SolidFill(1)),
			Dot((8,8),SolidFill(1)),
			Dot((9,10),SolidFill(1))
			]))

