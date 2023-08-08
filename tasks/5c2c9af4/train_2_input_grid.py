from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((23,23)),
		Dot((4,12),SolidFill(3)),
        Dot((8,8),SolidFill(3)),
        Dot((12,4),SolidFill(3)),
		]))
