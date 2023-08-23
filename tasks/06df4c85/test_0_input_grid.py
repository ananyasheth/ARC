from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((26,26)),
			Line(((2,0),(2,25)),SolidFill(4)),
            Line(((5,0),(5,25)),SolidFill(4)),
            Line(((8,0),(8,25)),SolidFill(4)),
            Line(((11,0),(11,25)),SolidFill(4)),
            Line(((14,0),(14,25)),SolidFill(4)),
            Line(((17,0),(17,25)),SolidFill(4)),
            Line(((20,0),(20,25)),SolidFill(4)),
            Line(((23,0),(23,25)),SolidFill(4)),
            Line(((0,2),(25,2)),SolidFill(4)),
            Line(((0,5),(25,5)),SolidFill(4)),
            Line(((0,8),(25,8)),SolidFill(4)),
            Line(((0,11),(25,11)),SolidFill(4)),
            Line(((0,14),(25,14)),SolidFill(4)),
            Line(((0,17),(25,17)),SolidFill(4)),
            Line(((0,20),(25,20)),SolidFill(4)),
            Line(((0,23),(25,23)),SolidFill(4)),
            Rectangle(((3,6),(4,7)),SolidFill(8)),
            Rectangle(((3,15),(4,16)),SolidFill(2)),
            Rectangle(((9,21),(10,22)),SolidFill(3)),
            Rectangle(((12,6),(13,7)),SolidFill(8)),
            Rectangle(((18,3),(19,4)),SolidFill(2)),
            Rectangle(((18,15),(19,16)),SolidFill(2)),
			]))
