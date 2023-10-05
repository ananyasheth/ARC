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
    self.__class__ = updatedGroupOfShapes.__class__
    self.__dict__ = updatedGroupOfShapes.__dict__
  
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
          
  def check_colour(self,shape,colour):
      for shape_colour in colour:
        if shape.fill.colour == shape_colour:
          return True
  
  def fetch_shape(self,kind=None,coordinates=None, colour=None):
    fetched_shapes=[]
    for shape in self.shapes:
      if coordinates is not None and kind is None and colour is None:
        if self.check_coordinates(shape,coordinates):
          fetched_shapes.append(shape)
      elif kind is not None and coordinates is None and colour is None:
        if self.check_kind(shape,kind):
          fetched_shapes.append(shape)
      elif colour is not None and coordinates is None and kind is None:
        if self.check_colour(shape,colour):
          fetched_shapes.append(shape)
      elif colour is not None and coordinates is not None and kind is None:
        if self.check_colour(shape,colour) and self.check_coordinates(shape,coordinates):
          fetched_shapes.append(shape)
      elif colour is not None and kind is not None and coordinates is None:
        if self.check_colour(shape,colour) and self.check_kind(shape,kind):
          fetched_shapes.append(shape)
      elif coordinates is not None and kind is not None and colour is None:
        if self.check_coordinates(shape,coordinates) and self.check_kind(shape,kind):
          fetched_shapes.append(shape)
      else:
        if self.check_coordinates(shape,coordinates) and self.check_kind(shape,kind) and self.check_colour(shape,colour):
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

  def rotate(self,around_point,degrees):
    for shape in self.shapes:
      shape.rotate(around_point,degrees)
    self.updateGroupOfShapes()
    
  def flip(self,axis,grid_dimensions):
    for shape in self.shapes:
      shape.flip(axis,grid_dimensions)
    self.updateGroupOfShapes()

  def bounce(self,initial_point,inflection_point,final_point,colour):
    return([Line((initial_point,inflection_point),SolidFill(colour)),Line((inflection_point,final_point),SolidFill(colour))])

  def extend(self, background_size, start_coordinates, direction, colour):
    (bg_x, bg_y) = background_size
    (x, y) = start_coordinates
    (x2, y2) = (x, y)
    # Iterate to find the last point of the diagonal line based on the direction
    if direction == "top-left":
      while x2 > 0 and y2 > 0:
        x2 -= 1
        y2 -= 1
    elif direction == "top-right":
      while x2 > 0 and y2 < bg_y - 1:
        x2 -= 1
        y2 += 1
    elif direction == "bottom-left":
      while x2 < bg_x - 1 and y2 > 0:
        x2 += 1
        y2 -= 1
    elif direction == "bottom-right":
      while x2 < bg_x - 1 and y2 < bg_y - 1:
        x2 += 1
        y2 += 1
    elif direction == "top":
      while x2 > 0 :
        x2 -= 1
    elif direction == "bottom":
      while x2 < bg_x - 1:
        x2 += 1
    elif direction == "left":
      while y2>0:
        y2 -= 1
    elif direction == "right":
      while y2 < bg_y - 1:
        y2 += 1
    return (Line(((x,y),(x2,y2)),SolidFill(colour)))


  def join(self, point_1_coordinates, point_2_coordinates, join_type, colour):
    (x1, y1) = point_1_coordinates
    (x2, y2) = point_2_coordinates

    # Iterate to find the last point of the diagonal line based on the direction
    if join_type == "straight-line":
      polyline = Polyline(((x1,y1),(x2,y2)),SolidFill(colour))
    elif join_type == "right-angle":
      if x2 >x1 and y2 >y1:
        polyline = Polyline(((x1,y1),(x1,y2),(x2,y2)),SolidFill(colour))
      elif x2 >x1 and y2==y1:
        polyline = Polyline(((x1,y1),(int(x2/2),int(y1+(x2/2))),(x2,y2)),SolidFill(colour))
      elif x2 >x1 and y2<y1:
        polyline = Polyline(((x1,y1),(x2,y1),(x2,y2)),SolidFill(colour))
      elif x2 <x1 and y2 >y1: 
        polyline = Polyline(((x1,y1),(x1,y2),(x2,y2)),SolidFill(colour))
      elif x2 <x1 and y2==y1:
        polyline = Polyline(((x2,y2),(int(x1/2),int(y2+(x1/2))),(x1,y1)),SolidFill(colour))
      else: 
        polyline = Polyline(((x1,y1),(x2,y1),(x2,y2)),SolidFill(colour))
    else:                                                                         # left angle
      if x2 >x1 and y2 >y1:
        polyline = Polyline(((x1,y1),(x2,y1),(x2,y2)),SolidFill(colour))
      elif x2 >x1 and y2==y1:
        polyline = Polyline(((x1,y1),(int(x2/2),int(y1-(x2/2))),(x2,y2)),SolidFill(colour))
      elif x2 >x1 and y2<y1:
        polyline = Polyline(((x1,y1),(x1,y2),(x2,y2)),SolidFill(colour))
      elif x2 <x1 and y2 >y1: 
        polyline = Polyline(((x1,y1),(x2,y1),(x2,y2)),SolidFill(colour))
      elif x2 <x1 and y2==y1:
        polyline = Polyline(((x2,y2),(int(x1/2),int(y2-(x1/2))),(x1,y1)),SolidFill(colour))
      else: 
        polyline = Polyline(((x1,y1),(x1,y2),(x2,y2)),SolidFill(colour))
    return (polyline)

  def return_shape_list_coordinates(self, shape_list):
    min_x, min_y, max_x, max_y = None, None, None, None
    for shape in shape_list:
      if min_x is None or shape.min_x < min_x:
        min_x = shape.min_x
      if min_y is None or shape.min_y < min_y:
        min_y = shape.min_y
      if max_x is None or shape.max_x > max_x:
        max_x = shape.max_x
      if max_y is None or shape.max_y > max_y:
        max_y = shape.max_y
    return (min_x, min_y, max_x, max_y)
