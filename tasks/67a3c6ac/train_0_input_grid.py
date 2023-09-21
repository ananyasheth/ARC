from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((4,4)),
            GroupOfShapes([
                Line(((0,0),(0,1)),SolidFill(6)),
                Dot((1,0),SolidFill(6)),
                Dot((1,1),SolidFill(1)),
                Dot((2,0),SolidFill(7)),
                Dot((2,1),SolidFill(2)),
                Dot((3,0),SolidFill(1)),
                Dot((3,1),SolidFill(7)),
            ]),
            GroupOfShapes([
                Line(((0,2),(1,2)),SolidFill(6)),
                Dot((2,2),SolidFill(7)),
                Line(((0,3),(3,3)),SolidFill(2)),
                Dot((3,2),SolidFill(2))
            ])
			]))

