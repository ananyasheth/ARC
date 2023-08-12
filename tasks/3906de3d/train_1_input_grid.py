from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((10,10)),
			Line(((0,2),(3,2)),SolidFill(1)),
            Line(((0,3),(3,3)),SolidFill(1)),
            Line(((0,4),(0,4)),SolidFill(1)),
            Line(((0,5),(3,5)),SolidFill(1)),
            Line(((0,6),(1,6)),SolidFill(1)),
            Line(((0,7),(4,7)),SolidFill(1)),
            Line(((0,8),(4,8)),SolidFill(1)),
            Line(((9,4),(9,4)),SolidFill(2)),
            Line(((6,6),(9,6)),SolidFill(2)),
			]))
