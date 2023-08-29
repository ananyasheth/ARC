from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((16,14)),
            GroupOfShapes([
                Rectangle(((1,1),(3,3)),SolidFill(5)),
                Polyline(((2,1),(3,1),(3,2)),SolidFill(3))
            ]),
            GroupOfShapes([
                Rectangle(((2,5),(4,7)),SolidFill(5)),
                Polyline(((2,6),(2,7),(3,7)),SolidFill(8))
            ]),
            GroupOfShapes([
                Rectangle(((0,11),(2,13)),SolidFill(5)),
                Tshape(((0,13),(2,13),(1,12),(1,13)),SolidFill(4))
            ]),
            GroupOfShapes([
                Rectangle(((5,10),(7,12)),SolidFill(5)),
                Polyline(((6,12),(7,12),(7,11)),SolidFill(9))
            ]),
            GroupOfShapes([
                Rectangle(((8,1),(10,3)),SolidFill(5)),
                Tshape(((8,1),(8,3),(8,2),(9,2)),SolidFill(1))
            ]),
            GroupOfShapes([
                Rectangle(((8,6),(10,8)),SolidFill(5)),
            ]),
            GroupOfShapes([
                Rectangle(((9,10),(11,12)),SolidFill(5)),
                Tshape(((9,10),(11,10),(10,10),(10,11)),SolidFill(6))
            ]),
            GroupOfShapes([
                Rectangle(((12,4),(14,6)),SolidFill(5)),
                Polyline(((12,5),(12,4),(13,4)),SolidFill(7))
            ]),
            GroupOfShapes([
                Rectangle(((13,9),(15,11)),SolidFill(5)),
                Tshape(((15,9),(15,11),(14,10),(15,10)),SolidFill(2))
            ])
			]))