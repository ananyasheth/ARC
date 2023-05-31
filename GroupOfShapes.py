from ImageMatrix import *
from Shape import *
from Fill import *

class GroupOfShapes(Shape):

  def __init__(self,shapes):
    self.shapes = shapes
    ImageMatrix.__init__(self,shapes[0].matrix,(shapes[0].x_offset,shapes[0].y_offset))
    for s in shapes[1:]:
      self.add_on_top(s)
    self.kind = 'GroupOfShapes'

  def largest(self,kind):
    lg = None
    for shape in self.shapes:
      if shape.kind==kind:
        if not(lg):
          lg = shape
          continue
        if shape>lg:
          lg = shape
    return(lg)
    
  def fetch_shape(self,kind):
    fetched_shapes=[]
    for shape in self.shapes:
      for shape_kind in kind:
        if shape.kind==shape_kind:
          fetched_shapes.append(shape)
    if len(fetched_shapes)==1:
      return fetched_shapes[0]
    else:
      return fetched_shapes
            
  def intersection_of_lines(self,list_of_lines):
    intersection_points = []
    for each_line in list_of_lines:
      if each_line.kind == 'HLine':
        x_value=each_line.min_x
        min_y=each_line.min_y
        max_y=each_line.max_y
        for each_line in list_of_lines:
          if each_line.kind == 'VLine':
            y_value=each_line.min_y
            min_x=each_line.min_x
            max_x=each_line.max_x
            for y_values in range(min_y,max_y):
              for x_values in range(min_x,max_x):
                if (x_value,y_values)==(x_values,y_value):
                  intersection_points.append((x_value,y_value))
    return intersection_points
          
  def split_matrix(self,row=0,column=0):
    if row==0:
      left_matrix = self.matrix[:, :column+1]
      right_matrix = self.matrix[:, column+1:]
      return left_matrix,right_matrix
    if column==0:
      top_matrix = self.matrix[:row+1, :]
      bottom_matrix = self.matrix[row+1:, :]
      return top_matrix,bottom_matrix

