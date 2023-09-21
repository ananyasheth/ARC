from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((22,22)),
			Rectangle(((0,0),(1,14)),SolidFill(1)),
            Rectangle(((0,16),(1,19)),SolidFill(1)),
            Rectangle(((0,21),(1,21)),SolidFill(1)),

			Rectangle(((3,0),(6,14)),SolidFill(1)),
            Rectangle(((3,16),(6,19)),SolidFill(1)),
            Rectangle(((3,21),(6,21)),SolidFill(1)),

			Rectangle(((8,0),(11,14)),SolidFill(1)),
            Rectangle(((8,16),(11,19)),SolidFill(1)),
            Rectangle(((8,21),(11,21)),SolidFill(1)),

			Rectangle(((13,0),(16,14)),SolidFill(1)),
            Rectangle(((13,16),(16,19)),SolidFill(1)),
            Rectangle(((13,21),(16,21)),SolidFill(1)),

			Rectangle(((18,0),(21,14)),SolidFill(1)),
            Rectangle(((18,16),(21,19)),SolidFill(1)),
            Rectangle(((18,21),(21,21)),SolidFill(1)),

            Line(((0,15),(21,15)),SolidFill(5)),
            Line(((0,20),(21,20)),SolidFill(5)),
            Line(((2,0),(2,21)),SolidFill(5)),
            Line(((7,0),(7,21)),SolidFill(5)),
            Line(((12,0),(12,21)),SolidFill(5)),
            Line(((17,0),(17,21)),SolidFill(5)),


			]))