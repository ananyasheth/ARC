from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,8)),
            GroupOfShapes(
[                Dot((0,0),SolidFill(2)),
                Dot((1,1),SolidFill(2)),
                Dot((1,2),SolidFill(4)),
                Dot((2,1),SolidFill(4)),
                Dot((2,2),SolidFill(2)),
                Dot((0,3),SolidFill(4)),
                Dot((3,0),SolidFill(4)),
                Dot((3,3),SolidFill(2)),]
            ),
            GroupOfShapes(
[                Line(((0,6),(3,6)),SolidFill(8)),
                Line(((1,4),(1,7)),SolidFill(8)),]
            )
			]))