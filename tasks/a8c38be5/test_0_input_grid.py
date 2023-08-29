from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((16,15)),
            GroupOfShapes([
                Rectangle(((1,1),(3,3)),SolidFill(5)),
                Tshape(((1,1),(3,1),(2,1),(2,2)),SolidFill(1))
            ]),
            GroupOfShapes([
                Rectangle(((2,5),(4,7)),SolidFill(5)),
                Tshape(((2,5),(2,7),(2,6),(3,6)),SolidFill(2))
            ]),
            GroupOfShapes([
                Rectangle(((0,10),(2,12)),SolidFill(5)),
                Polyline(((1,10),(2,10),(2,11)),SolidFill(6))
            ]),
            GroupOfShapes([
                Rectangle(((6,2),(8,4)),SolidFill(5)),
                Tshape(((8,2),(8,4),(7,3),(8,3)),SolidFill(8))
            ]),
            GroupOfShapes([
                Rectangle(((7,6),(9,8)),SolidFill(5)),
                Tshape(((7,8),(9,8),(8,7),(8,8)),SolidFill(1))
            ]),
            GroupOfShapes([
                Rectangle(((5,10),(7,12)),SolidFill(5)),
            ]),
            GroupOfShapes([
                Rectangle(((10,1),(12,3)),SolidFill(5)),
                Polyline(((10,2),(10,3),(11,3)),SolidFill(4))
            ]),
            GroupOfShapes([
                Rectangle(((12,6),(14,8)),SolidFill(5)),
                Polyline(((13,8),(14,8),(14,7)),SolidFill(7))
            ]),
            GroupOfShapes([
                Rectangle(((10,11),(12,13)),SolidFill(5)),
                Polyline(((10,12),(10,11),(11,11)),SolidFill(3))
            ])
			]))