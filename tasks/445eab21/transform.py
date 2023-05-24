from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
	largest_rectangle = group_of_shapes.largest('RectangleOutline')
	return(GroupOfShapes([
			Background((2,2),SolidFill(largest_rectangle.fill.colour))
			]))
