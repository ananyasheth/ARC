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
            Dot(())
			]))

