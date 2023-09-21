from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((11,11)),
			Rectangle(((0,0),(2,3)),SolidFill(1)),
			Rectangle(((0,5),(2,10)),SolidFill(1)),
            Rectangle(((4,0),(8,3)),SolidFill(1)),
            Rectangle(((4,5),(8,10)),SolidFill(1)),
            Rectangle(((10,0),(10,3)),SolidFill(1)),
            Rectangle(((10,5),(10,10)),SolidFill(1)),
            Line(((0,4),(10,4)),SolidFill(8)),
            Line(((3,0),(3,10)),SolidFill(8)),
            Line(((9,0),(9,10)),SolidFill(8)),
			]))