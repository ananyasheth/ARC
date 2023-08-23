from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((23,23)),
			Line(((2,0),(2,22)),SolidFill(4)),
            Line(((5,0),(5,22)),SolidFill(4)),
            Line(((8,0),(8,22)),SolidFill(4)),
            Line(((11,0),(11,22)),SolidFill(4)),
            Line(((14,0),(14,22)),SolidFill(4)),
            Line(((17,0),(17,22)),SolidFill(4)),
            Line(((20,0),(20,22)),SolidFill(4)),
            Line(((0,2),(22,2)),SolidFill(4)),
            Line(((0,5),(22,5)),SolidFill(4)),
            Line(((0,8),(22,8)),SolidFill(4)),
            Line(((0,11),(22,11)),SolidFill(4)),
            Line(((0,14),(22,14)),SolidFill(4)),
            Line(((0,17),(22,17)),SolidFill(4)),
            Line(((0,20),(22,20)),SolidFill(4)),
            Rectangle(((3,3),(4,4)),SolidFill(3)),
            Rectangle(((3,15),(4,16)),SolidFill(2)),
            Rectangle(((9,9),(10,10)),SolidFill(2)),
            Rectangle(((9,18),(10,19)),SolidFill(2)),
            Rectangle(((18,3),(19,4)),SolidFill(3)),
            Rectangle(((18,15),(19,16)),SolidFill(3)),
			]))
