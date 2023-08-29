from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
  new_group_of_shapes = []
  polylines = group_of_shapes.fetch_shape(['Polyline'])
  background = group_of_shapes.fetch_shape(['Background'])[0]
  background.updateColour(5)
  new_group_of_shapes.append(background)

  longest_polyline_length = 0
  longest_polyline_index = None
  for index, polyline in enumerate(polylines):
    if polyline.calculate_length() > longest_polyline_length:
      longest_polyline_length = polyline.calculate_length()
      longest_polyline_index = index
  longest_polyline = polylines[longest_polyline_index]
  new_group_of_shapes.append(longest_polyline)

  return GroupOfShapes(new_group_of_shapes)

