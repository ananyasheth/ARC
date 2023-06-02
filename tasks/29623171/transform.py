from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
  number_of_dots=[]
  background = group_of_shapes.fetch_shape(['Background'])
  lines = group_of_shapes.fetch_shape(['HLine','VLine'])
  dots = group_of_shapes.fetch_shape(['Dot'])
  intersection_points = group_of_shapes.intersection_of_lines(lines)
  unique_segments = group_of_shapes.segment_grid(intersection_points,3)
  for each_segment in unique_segments:
    dots_in_each_segment = group_of_shapes.fetch_shape(['Dot'],each_segment)
    if type(dots_in_each_segment)==list:
      number_of_dots.append(len(dots_in_each_segment))
    else:
      number_of_dots.append(1)
  max_value = max(number_of_dots)
  max_indices = [index for index, value in enumerate(number_of_dots) if value == max_value]
  new_group_of_shapes = [background]
  for each_line in lines:
    new_group_of_shapes.append(each_line)
  for each_index in max_indices:
    new_group_of_shapes.append(Rectangle(unique_segments[each_index],SolidFill(dots[0].fill.colour)))
  return GroupOfShapes(new_group_of_shapes)
