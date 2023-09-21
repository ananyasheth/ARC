from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((6,6)),
            GroupOfShapes([
                Dot((0,0),SolidFill(1)),
                Dot((0,1),SolidFill(2)),
                Dot((0,2),SolidFill(7)),
                Dot((1,0),SolidFill(2)),
                Dot((1,1),SolidFill(1)),
                Dot((1,2),SolidFill(7)),
                Dot((2,0),SolidFill(2)),
                Dot((2,1),SolidFill(1)),
                Dot((2,2),SolidFill(2)),
                Dot((3,0),SolidFill(1)),
                Dot((3,1),SolidFill(2)),
                Dot((3,2),SolidFill(1)),
                Dot((4,0),SolidFill(2)),
                Dot((4,1),SolidFill(7)),
                Dot((4,2),SolidFill(1)),
                Dot((5,0),SolidFill(2)),
                Dot((5,1),SolidFill(1)),
                Dot((5,2),SolidFill(6)),
            ]),
            GroupOfShapes([
                Line(((0,3),(0,5)),SolidFill(1)),
                Dot((1,3),SolidFill(7)),
                Dot((1,4),SolidFill(2)),
                Dot((1,5),SolidFill(6)),
                Dot((2,3),SolidFill(6)),
                Dot((2,4),SolidFill(2)),
                Dot((2,5),SolidFill(1)),
                Dot((3,3),SolidFill(7)),
                Dot((3,4),SolidFill(6)),
                Dot((3,5),SolidFill(2)),
                Dot((4,3),SolidFill(2)),
                Dot((4,4),SolidFill(7)),
                Dot((4,5),SolidFill(1)),
                Dot((5,3),SolidFill(2)),
                Dot((5,4),SolidFill(7)),
                Dot((5,5),SolidFill(7)),
            ]),
			]))