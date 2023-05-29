from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
    		Background((3,3)),
    		Line(((0,0),(0,1)),SolidFill(3)),
    		Line(((1,0),(1,2)),SolidFill(4)),
    		Dot((0,2),SolidFill(8)),
    		Dot((2,0),SolidFill(8)),
    		Line(((2,1),(2,2)),SolidFill(1))
  		]))
