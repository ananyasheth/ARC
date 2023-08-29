from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def input_grid():
        return(GroupOfShapes([
                Background((3,3)),
                Dot((0,0),SolidFill(1)),
                Dot((2,0),SolidFill(1)),
                Polyline(((0,1),(2,1),(1,0)),SolidFill(3)),
                Polyline(((0,2),(2,2)),SolidFill(2))
                ]))
