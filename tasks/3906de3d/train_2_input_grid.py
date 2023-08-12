from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Line(((0,1),(3,1)),SolidFill(1)),
            Line(((0,2),(3,2)),SolidFill(1)),
            Line(((0,3),(0,3)),SolidFill(1)),
            Line(((0,4),(2,4)),SolidFill(1)),
            Line(((0,5),(3,5)),SolidFill(1)),
            Line(((0,6),(2,6)),SolidFill(1)),
            Line(((0,7),(3,7)),SolidFill(1)),
            Line(((0,8),(1,8)),SolidFill(1)),
            Line(((0,9),(3,9)),SolidFill(1)),
            Line(((7,3),(9,3)),SolidFill(2)),
            Line(((8,4),(9,4)),SolidFill(2)),
            Line(((6,6),(9,6)),SolidFill(2)),
            Line(((7,8),(9,8)),SolidFill(2)),
			]))
