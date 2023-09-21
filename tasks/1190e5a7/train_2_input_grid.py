from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((27,27)),
			Rectangle(((0,0),(1,5)),SolidFill(3)),
            Rectangle(((0,7),(1,20)),SolidFill(3)),
            Rectangle(((0,22),(1,22)),SolidFill(3)),
            Rectangle(((0,24),(1,24)),SolidFill(3)),
            Rectangle(((0,26),(1,26)),SolidFill(3)),

			Rectangle(((3,0),(6,5)),SolidFill(3)),
            Rectangle(((3,7),(6,20)),SolidFill(3)),
            Rectangle(((3,22),(6,22)),SolidFill(3)),
            Rectangle(((3,24),(6,24)),SolidFill(3)),
            Rectangle(((3,26),(6,26)),SolidFill(3)),

            Rectangle(((8,0),(15,5)),SolidFill(3)),
            Rectangle(((8,7),(15,20)),SolidFill(3)),
            Rectangle(((8,22),(15,22)),SolidFill(3)),
            Rectangle(((8,24),(15,24)),SolidFill(3)),
            Rectangle(((8,26),(15,26)),SolidFill(3)),

            Rectangle(((17,0),(20,5)),SolidFill(3)),
            Rectangle(((17,7),(20,20)),SolidFill(3)),
            Rectangle(((17,22),(20,22)),SolidFill(3)),
            Rectangle(((17,24),(20,24)),SolidFill(3)),
            Rectangle(((17,26),(20,26)),SolidFill(3)),

            Rectangle(((22,0),(22,5)),SolidFill(3)),
            Rectangle(((22,7),(22,20)),SolidFill(3)),
            Rectangle(((22,22),(22,22)),SolidFill(3)),
            Rectangle(((22,24),(22,24)),SolidFill(3)),
            Rectangle(((22,26),(22,26)),SolidFill(3)),

            Rectangle(((24,0),(26,5)),SolidFill(3)),
            Rectangle(((24,7),(26,20)),SolidFill(3)),
            Rectangle(((24,22),(26,22)),SolidFill(3)),
            Rectangle(((24,24),(26,24)),SolidFill(3)),
            Rectangle(((24,26),(26,26)),SolidFill(3)),

            Line(((0,6),(26,6)),SolidFill(1)),
            Line(((0,21),(26,21)),SolidFill(1)),
            Line(((0,23),(26,23)),SolidFill(1)),
            Line(((0,25),(26,25)),SolidFill(1)),
            Line(((2,0),(2,26)),SolidFill(1)),
            Line(((7,0),(7,26)),SolidFill(1)),
            Line(((16,0),(16,26)),SolidFill(1)),
            Line(((21,0),(21,26)),SolidFill(1)),
            Line(((23,0),(23,26)),SolidFill(1)),

			]))