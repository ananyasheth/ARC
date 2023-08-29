from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
    		Background((3,3)),
    		Polyline(((0,0),(0,1)),SolidFill(3)),
    		Polyline(((1,0),(1,2)),SolidFill(4)),
    		Dot((0,2),SolidFill(8)),
    		Dot((2,0),SolidFill(8)),
    		Polyline(((2,1),(2,2)),SolidFill(1))
  		]))