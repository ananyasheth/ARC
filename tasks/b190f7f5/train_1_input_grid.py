from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,6)),
            GroupOfShapes(
[               Line(((1,0),(2,0)),SolidFill(8)),
                Line(((2,0),(2,1)),SolidFill(8)),
                Line(((0,2),(0,2)),SolidFill(8))]
            ),
            GroupOfShapes(
[                Dot((0,4),SolidFill(4)),
                Dot((1,4),SolidFill(2)),
                Dot((1,3),SolidFill(1)),
                Dot((2,4),SolidFill(1)),
                Dot((1,5),SolidFill(4)),]
            )
			]))