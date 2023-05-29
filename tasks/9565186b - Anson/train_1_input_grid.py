from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
    Background((3,3)),
    Line(((0,0),(0,2)),SolidFill(1)),
    Line(((1,0),(2,0)),SolidFill(8)),
    Dot((1,1),SolidFill(1)),
    Dot((1,2),SolidFill(3)),
    Line(((2,1),(2,2)),SolidFill(2))
  ]))
