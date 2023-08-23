from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((20,20)),
			Line(((2,0),(2,19)),SolidFill(8)),
            Line(((5,0),(5,19)),SolidFill(8)),
            Line(((8,0),(8,19)),SolidFill(8)),
            Line(((11,0),(11,19)),SolidFill(8)),
            Line(((14,0),(14,19)),SolidFill(8)),
            Line(((17,0),(17,19)),SolidFill(8)),
            Line(((0,2),(19,2)),SolidFill(8)),
            Line(((0,5),(19,5)),SolidFill(8)),
            Line(((0,8),(19,8)),SolidFill(8)),
            Line(((0,11),(19,11)),SolidFill(8)),
            Line(((0,14),(19,14)),SolidFill(8)),
            Line(((0,17),(19,17)),SolidFill(8)),
            Rectangle(((3,3),(4,4)),SolidFill(2)),
            Rectangle(((3,15),(4,16)),SolidFill(2)),
            Rectangle(((6,9),(7,10)),SolidFill(1)),
            Rectangle(((9,15),(10,16)),SolidFill(2)),
            Rectangle(((12,3),(13,4)),SolidFill(3)),
            Rectangle(((12,9),(13,10)),SolidFill(3)),
			]))
