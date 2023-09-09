from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
			Background((9,9)),
			GroupOfShapes([			
				Dot((0,0),SolidFill(8)),
            	Dot((0,1),SolidFill(8)),
            	Dot((1,2),SolidFill(8)),
            	Dot((2,0),SolidFill(8)),
			])
			]))
