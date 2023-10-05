from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,10)),
            Rectangle(((1,1),(2,2)),SolidFill(5)),
            Rectangle(((1,4),(2,5)),SolidFill(5)),
            Rectangle(((4,5),(5,6)),SolidFill(5)),
            Line(((1,3),(3,3)),SolidFill(5)),
            Line(((1,6),(3,6)),SolidFill(5)),
            Line(((4,4),(6,4)),SolidFill(5)),
            
            ])
			)