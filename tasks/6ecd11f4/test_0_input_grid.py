from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
    return(GroupOfShapes([
			Background((21,24)),
            Rectangle(((1,2),(3,4)),SolidFill(2)),
            Rectangle(((4,5),(6,7)),SolidFill(2)),
            Rectangle(((4,8),(6,10)),SolidFill(2)),
            Rectangle(((1,8),(3,10)),SolidFill(2)),
            Rectangle(((1,11),(3,13)),SolidFill(2)),
            Rectangle(((7,2),(9,4)),SolidFill(2)),
            Rectangle(((10,2),(12,4)),SolidFill(2)),
            Rectangle(((7,5),(9,7)),SolidFill(2)),
            Rectangle(((7,8),(9,10)),SolidFill(2)),
            Rectangle(((7,11),(9,13)),SolidFill(2)),
            Rectangle(((10,11),(12,13)),SolidFill(2)),

            Dot((15,15),SolidFill(4)),
            Dot((15,16),SolidFill(8)),
            Dot((15,17),SolidFill(6)),
            Dot((15,18),SolidFill(3)),
            Dot((16,15),SolidFill(9)),
            Dot((16,16),SolidFill(3)),
            Dot((16,17),SolidFill(3)),
            Dot((16,18),SolidFill(5)),
            Dot((17,15),SolidFill(6)),
            Dot((17,16),SolidFill(7)),
            Dot((17,17),SolidFill(7)),
            Dot((17,18),SolidFill(4)),
            Dot((18,15),SolidFill(1)),
            Dot((18,16),SolidFill(5)),
            Dot((18,17),SolidFill(8)),
            Dot((18,18),SolidFill(1)),
            ]))
