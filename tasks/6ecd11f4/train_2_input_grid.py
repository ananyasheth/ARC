from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((22,22)),
            Rectangle(((1,2),(4,5)),SolidFill(8)),
            Rectangle(((5,2),(8,5)),SolidFill(8)),
            Rectangle(((9,2),(12,5)),SolidFill(8)),
            Rectangle(((13,2),(16,5)),SolidFill(8)),
            Rectangle(((13,6),(16,9)),SolidFill(8)),
            Rectangle(((13,10),(16,13)),SolidFill(8)),
            Rectangle(((1,10),(4,13)),SolidFill(8)),
            Rectangle(((5,10),(8,13)),SolidFill(8)),
            Rectangle(((1,14),(4,17)),SolidFill(8)),
            Rectangle(((9,14),(12,17)),SolidFill(8)),

            Dot((16,17),SolidFill(4)),
            Dot((16,18),SolidFill(1)),
            Dot((16,19),SolidFill(9)),
            Dot((16,20),SolidFill(4)),
            Dot((17,17),SolidFill(6)),
            Dot((17,18),SolidFill(3)),
            Dot((17,19),SolidFill(6)),
            Dot((17,20),SolidFill(1)),
            Dot((18,17),SolidFill(3)),
            Dot((18,18),SolidFill(5)),
            Dot((18,19),SolidFill(7)),
            Dot((18,20),SolidFill(5)),
            Dot((19,17),SolidFill(2)),
            Dot((19,18),SolidFill(4)),
            Dot((19,19),SolidFill(2)),
            Dot((19,20),SolidFill(7)),

            ]))
