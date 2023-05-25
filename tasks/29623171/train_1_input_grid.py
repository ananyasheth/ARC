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
                        Dot((1,0),SolidFill(2)),
	                Dot((0,5),SolidFill(2)),
		        Dot((0,8),SolidFill(2)),
		        Dot((1,10),SolidFill(2)),
			Dot((4,0),SolidFill(2)),
			Dot((5,0),SolidFill(2)),
			Dot((5,6),SolidFill(2)),
			Dot((6,9),SolidFill(2)),
			Dot((9,0),SolidFill(2)),
			Dot((9,6),SolidFill(2)),
			Dot((9,10),SolidFill(2))
			]))

