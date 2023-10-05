from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((8,4)),
            GroupOfShapes(
[                Dot((0,0),SolidFill(3)),
                Dot((1,1),SolidFill(2)),
                Dot((1,2),SolidFill(2)),
                Dot((2,1),SolidFill(2)),
                Dot((2,2),SolidFill(2)),
                Dot((0,3),SolidFill(1)),
                Dot((3,0),SolidFill(3)),
                Dot((3,3),SolidFill(3)),]
            ),
            GroupOfShapes(
[                Line(((4,1),(4,2)),SolidFill(8)),
                Line(((5,0),(5,3)),SolidFill(8)),
                Line(((5,0),(7,0)),SolidFill(8)),
                Line(((7,0),(7,3)),SolidFill(8)),
                Line(((5,3),(7,3)),SolidFill(8)),]
            )
			]))