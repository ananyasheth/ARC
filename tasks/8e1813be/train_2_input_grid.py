from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((12,12)),
            Line(((1,0),(1,11)),SolidFill(2)),
            Line(((4,0),(4,11)),SolidFill(8)),
            Line(((7,0),(7,11)),SolidFill(4)),
            Line(((10,0),(10,11)),SolidFill(1)),
            Rectangle(((1,6),(4,9)),SolidFill(5)),
            RectangleOutline(((0,5),(5,10)),SolidFill(0))
			]))

# encode one red straight line
# encode black rectangle outline on top