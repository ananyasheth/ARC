from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,11)),
            Rectangle(((1,2),(2,3)),SolidFill(5)),
            Rectangle(((3,4),(4,5)),SolidFill(5)),
            Rectangle(((4,6),(5,7)),SolidFill(5)),
            Line(((2,4),(2,6)),SolidFill(5)),
            Line(((3,3),(5,3)),SolidFill(5)),
            Line(((6,5),(6,7)),SolidFill(5)),
            ])
			)

