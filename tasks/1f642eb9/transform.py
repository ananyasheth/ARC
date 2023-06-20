from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
  print(group_of_shapes.matrix)
  group_of_shapes.shapes[1].scale(2,2)
  updatedGroupOfShapes = group_of_shapes.updateGroupOfShapes()
  print(updatedGroupOfShapes.matrix)
  return updatedGroupOfShapes
