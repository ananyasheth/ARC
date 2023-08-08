from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((23,23)),
		Dot((2,11),SolidFill(8)),
        Dot((5,14),SolidFill(8)),
        Dot((8,17),SolidFill(8)),
		]))
