from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,11)),
            Rectangle(((0,2),(1,3)),SolidFill(5)),
            Rectangle(((2,4),(3,5)),SolidFill(5)),
            Rectangle(((5,5),(6,6)),SolidFill(5)),
            Line(((2,1),(2,3)),SolidFill(5)),
            Line(((0,5),(0,7)),SolidFill(5)),
            Line(((0,6),(3,6)),SolidFill(5)),
            Line(((4,3),(4,5)),SolidFill(5)),
            
            ])
			)