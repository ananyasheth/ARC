from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Line(((0,1),(3,1)),SolidFill(1)),
            Line(((0,2),(0,2)),SolidFill(1)),
            Line(((0,3),(4,3)),SolidFill(1)),
            Line(((0,4),(1,4)),SolidFill(1)),
            Line(((0,5),(2,5)),SolidFill(1)),
            Line(((0,6),(1,6)),SolidFill(1)),
            Line(((0,7),(3,7)),SolidFill(1)),
            Line(((0,8),(0,8)),SolidFill(1)),
            Line(((0,9),(4,9)),SolidFill(1)),
            Line(((7,2),(9,2)),SolidFill(2)),
            Line(((8,4),(9,4)),SolidFill(2)),
            Line(((6,5),(9,5)),SolidFill(2)),
            Line(((9,6),(9,6)),SolidFill(2)),
            Line(((4,8),(9,8)),SolidFill(2)),
			]))
