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
  
  def updateGroupOfShapes(self):
    updatedshapes = []
    for shapes in self.shapes:
      updatedshapes.append(shapes)
    updatedGroupOfShapes = GroupOfShapes(updatedshapes)
    return updatedGroupOfShapes
    
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

  def check_coordinates(self,shape,coordinates):
    ((coordx1,coordy1),(coordx2,coordy2))=coordinates
    if coordx1<=shape.min_x<=coordx2 and coordx1<=shape.max_x<=coordx2 and coordy1<=shape.min_y<=coordy2 and coordy1<=shape.max_y<=coordy2:
      return True
    
  def check_kind(self,shape,kind):
      for shape_kind in kind:
        if shape.kind==shape_kind:
          return True
    
  def fetch_shape(self,kind=None,coordinates=None):
    fetched_shapes=[]
    for shape in self.shapes:
      if coordinates is not None and kind is None:
        if self.check_coordinates(shape,coordinates):
          fetched_shapes.append(shape)
      elif kind is not None and coordinates is None:
        if self.check_kind(shape,kind):
          fetched_shapes.append(shape)
      else:
        if self.check_coordinates(shape,coordinates) and self.check_kind(shape,kind):
          fetched_shapes.append(shape)
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
    
  def segment_grid(self,intersection_points,segment_size):
    segments = []
    for each_points_pair in intersection_points:
      segments.append(((each_points_pair[0]-segment_size,each_points_pair[1]-segment_size),(each_points_pair[0]-1,each_points_pair[1]-1)))
      segments.append(((each_points_pair[0]+1,each_points_pair[1]+1),(each_points_pair[0]+segment_size,each_points_pair[1]+segment_size)))
      segments.append(((each_points_pair[0]-segment_size,each_points_pair[1]+1),(each_points_pair[0]-1,each_points_pair[1]+segment_size)))
      segments.append(((each_points_pair[0]+1,each_points_pair[1]-segment_size),(each_points_pair[0]+segment_size,each_points_pair[1]-1)))
    unique_segments = list(dict.fromkeys(segments))
    return unique_segments
    
  def count_shapes(self,segment,shape):
    for x in range(segment.min_x,segment.max_x+1):
      for y in range(segment.min_y,segment.max_y+1):
        for each_shape in shape:
          if shape.min_x==x or shape.min_y==y:
            segment.subshape.append(each_shape)
    return len(segment.subshape)
    
  def split_matrix(self,row=0,column=0):
    if row==0:
      left_matrix = self.matrix[:, :column+1]
      right_matrix = self.matrix[:, column+1:]
      return left_matrix,right_matrix
    if column==0:
      top_matrix = self.matrix[:row+1, :]
      bottom_matrix = self.matrix[row+1:, :]
      return top_matrix,bottom_matrix

