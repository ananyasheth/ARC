from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
  new_group_of_shapes = []
  most_color_shape = group_of_shapes.most_color_shape
  background = group_of_shapes.fetch_shape(kind=['Background'])
  dots = group_of_shapes.fetch_shape(kind=['Dot'])
  lines = group_of_shapes.fetch_shape(kind=['Line'])

  for shape in group_of_shapes.shapes:
    if shape != most_color_shape:
      shape.fill.colour = 5
    new_group_of_shapes.append(shape)

  return GroupOfShapes(new_group_of_shapes)