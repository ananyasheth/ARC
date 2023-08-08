from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
	return(GroupOfShapes([
		Background((23,23)),
		Dot((15,9),SolidFill(2)),
        Dot((13,11),SolidFill(2)),
        Dot((11,13),SolidFill(2)),
		]))
