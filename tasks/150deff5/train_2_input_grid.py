from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,9)),
            Rectangle(((1,4),(2,5)),SolidFill(5)),
            Rectangle(((4,4),(5,5)),SolidFill(5)),
            
            Line(((1,1),(1,3)),SolidFill(5)),
            Line(((3,3),(5,3)),SolidFill(5)),
            
            
            ])
			)