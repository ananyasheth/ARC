from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((3,6)),
            GroupOfShapes([
                Dot((0,0),SolidFill(2)),
                Dot((1,1),SolidFill(3)),
                Dot((0,2),SolidFill(4))
            ]),
            GroupOfShapes([
                Line(((0,4),(2,4)),SolidFill(8)),
                Line(((1,3),(1,5)),SolidFill(8))]
            )
			]))

