from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((14,14)),
            GroupOfShapes([
                Rectangle(((0,0),(2,2)),SolidFill(5)),
                Polyline(((1,0),(2,0),(2,1)),SolidFill(8))
            ]),
            GroupOfShapes([
                Rectangle(((3,2),(5,4)),SolidFill(5)),
                Tshape(((3,2),(5,2),(4,2),(4,3)),SolidFill(2))
            ]),
            GroupOfShapes([
                Rectangle(((7,1),(9,3)),SolidFill(5)),
                Polyline(((7,2),(7,3),(8,3)),SolidFill(1))
            ]),
            GroupOfShapes([
                Rectangle(((11,0),(13,2)),SolidFill(5)),
                Polyline(((12,2),(13,2),(13,1)),SolidFill(9))
            ]),
            GroupOfShapes([
                Rectangle(((1,8),(3,10)),SolidFill(5)),
                Tshape(((1,8),(1,10),(1,9),(2,9)),SolidFill(2))
            ]),
            GroupOfShapes([
                Rectangle(((5,6),(7,8)),SolidFill(5)),
            ]),
            GroupOfShapes([
                Rectangle(((6,10),(8,12)),SolidFill(5)),
                Tshape(((8,10),(8,12),(7,11),(8,11)),SolidFill(4))
            ]),
            GroupOfShapes([
                Rectangle(((9,6),(11,8)),SolidFill(5)),
                Tshape(((9,8),(11,8),(10,7),(10,8)),SolidFill(3))
            ]),
            GroupOfShapes([
                Rectangle(((11,10),(13,12)),SolidFill(5)),
                Polyline(((11,11),(11,10),(12,10)),SolidFill(6))
            ])
			]))
