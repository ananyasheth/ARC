from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((7,7)),
            GroupOfShapes([
                Polyline(((0,0),(0,2),(1,1),(2,1),(2,0)),SolidFill(7)),
                Dot((1,0),SolidFill(6)),
                Dot((1,2),SolidFill(1)),
                Dot((2,2),SolidFill(2)),
                Polyline(((3,0),(3,1),(4,1)),SolidFill(2)),
                Dot((4,0),SolidFill(7)),
                Line(((3,2),(4,2)),SolidFill(7)),
                Polyline(((6,0),(5,0),(5,2),(6,2)),SolidFill(6)),
                Dot((6,1),SolidFill(2))
            ]),
            GroupOfShapes([
                Dot((0,3),SolidFill(6)),
                Line(((1,3),(2,3)),SolidFill(1)),
                Dot((3,3),SolidFill(7)),
                Dot((4,3),SolidFill(1)),
                Dot((5,3),SolidFill(2)),
                Dot((6,3),SolidFill(6)),
            ]),
            GroupOfShapes([
                Line(((0,4),(0,5)),SolidFill(6)),
                Dot((0,6),SolidFill(2)),
                Line(((1,4),(1,5)),SolidFill(7)),
                Dot((1,6),SolidFill(1)),
                Dot((2,4),SolidFill(2)),
                Line(((2,5),(2,6)),SolidFill(6)),
                Dot((3,4),SolidFill(7)),
                Line(((3,5),(3,6)),SolidFill(2)),
                Dot((4,4),SolidFill(2)),
                Dot((4,5),SolidFill(7)),
                Dot((4,6),SolidFill(2)),
                Dot((5,4),SolidFill(2)),
                Line(((5,5),(5,6)),SolidFill(1)),
                Line(((6,4),(6,6)),SolidFill(6)),
			])]))

