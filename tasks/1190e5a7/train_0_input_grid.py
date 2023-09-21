from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((15,15)),
			Rectangle(((0,0),(1,0)),SolidFill(3)),
			Rectangle(((0,2),(1,9)),SolidFill(3)),
            Rectangle(((0,11),(1,12)),SolidFill(3)),
            Rectangle(((0,14),(1,14)),SolidFill(3)),
            Rectangle(((3,0),(14,0)),SolidFill(3)),
            Rectangle(((3,2),(14,9)),SolidFill(3)),
            Rectangle(((3,11),(14,12)),SolidFill(3)),
            Rectangle(((3,14),(14,14)),SolidFill(3)),
            Line(((0,1),(14,1)),SolidFill(7)),
            Line(((0,10),(14,10)),SolidFill(7)),
            Line(((0,13),(14,13)),SolidFill(7)),
            Line(((2,0),(2,14)),SolidFill(7)),
			]))