import numpy as np
from ImageMatrix import *
from Fill import *

class Shape(ImageMatrix):
  pass

class Background(Shape):

  def __init__(self,size,fill=SolidFill(0)):
    (x_size,y_size) = size
    matrix = np.full((x_size,y_size),10)
    ImageMatrix.__init__(self,matrix)
    fill.apply(self)
    self.kind = 'Background'
    self.fill = fill

class Dot(Shape):

  def __init__(self,point,fill):
    (x,y) = point
    matrix = np.full((1,1),10)
    ImageMatrix.__init__(self,matrix,(x,y))
    fill.apply(self)
    self.kind = 'Dot'
    self.fill = fill

class Line(Shape):

  def __init__(self,points,fill):
    ((x1,y1),(x2,y2)) = points
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    x_size = max_x-min_x+1
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    y_size = max_y-min_y+1
    matrix = np.full((x_size,y_size),-1)
    if x_size==1: # horizontal line
      for y in range(min_y,max_y+1):
        matrix[0,y-min_y] = 10
      self.kind = 'HLine'
    elif y_size==1: # vertical line
      for x in range(min_x,max_x+1):
        matrix[x-min_x,0] = 10
      self.kind = 'VLine'
    else: # diagonal line
      x = min_x
      y = min_y
      while (x<=max_x and y<=max_y):
        matrix[x-min_x,y-min_y] = 10
        x += 1
        y += 1
      self.kind = 'DLine'
    ImageMatrix.__init__(self,matrix,(min_x,min_y))
    fill.apply(self)
    self.fill = fill

class Rectangle(Shape):

  def __init__(self,points,fill,subshape=None):
    ((x1,y1),(x2,y2)) = points
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    x_size = max_x-min_x+1
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    y_size = max_y-min_y+1
    matrix = np.full((x_size,y_size),10)
    ImageMatrix.__init__(self,matrix,(min_x,min_y))
    fill.apply(self)
    self.kind = 'Rectangle'
    self.fill = fill

  def __gt__(self,other):
    return(self.x_size*self.y_size>other.x_size*other.y_size)
    
    
class RectangleOutline(Shape): 

  def __init__(self,points,fill):
    ((x1,y1),(x2,y2)) = points
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    x_size = max_x-min_x+1
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    y_size = max_y-min_y+1
    matrix = np.full((x_size,y_size),-1)
    for x in range(min_x,max_x+1):
      matrix[x-min_x,0] = 10
      matrix[x-min_x,y_size-1] = 10
    for y in range(min_y,max_y+1):
      matrix[0,y-min_y] = 10
      matrix[x_size-1,y-min_y] = 10
    ImageMatrix.__init__(self,matrix,(min_x,min_y))
    fill.apply(self)
    self.kind = 'RectangleOutline'
    self.fill = fill

  def __gt__(self,other):
    return(self.x_size*self.y_size>other.x_size*other.y_size)

class Tshape(Shape):
  
  def __init__(self,points,fill):
    ((x1,y1),(x2,y2),(x3,y3)) = points    # x3,y3 T corner point
    min_x = min(x1,x2,x3)
    max_x = max(x1,x2,x3)
    x_size = max_x-min_x+1
    min_y = min(y1,y2,y3)
    max_y = max(y1,y2,y3)
    y_size = max_y-min_y+1
    matrix = np.full((x_size,y_size),-1)
    if x1 == x2:
      if x3 > x1:       # normal T
        matrix[:, int((max_y-min_y)/2)] = 10
        matrix[0, :] = 10
      else:             # inverted T
        matrix[:, int((max_y-min_y)/2)] = 10
        matrix[int((max_x-min_x)), :] = 10
    else:
      if y3 > y1:       # right T
        matrix[:, 0] = 10
        matrix[int((max_x-min_x)/2),:] = 10
      else:             # left T
        matrix[:, max_y-min_y] = 10
        matrix[int((max_x-min_x)/2),:] = 10
    
    ImageMatrix.__init__(self, matrix, (min_x, min_y))
    fill.apply(self)
    self.kind = 'Tshape'
    self.fill = fill


class Polyline(Shape):
  
  def __init__(self, points,fill):
    min_x = min(point[0] for point in points)              
    max_x = max(point[0] for point in points)
    x_size = max_x - min_x + 1
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    y_size = max_y - min_y + 1
    matrix = np.full((x_size, y_size), -1)

    # Connect the points to form the shape
    for point in range(len(points)):
      if point + 1 == len(points):
        break                       # connection stops between last point and first point
      else:
        x1, y1 = points[point]      # current point      
        x2, y2 = points[point + 1]  # next point
        dx = x2 - x1                                
        dy = y2 - y1

        # Move up                   # number of steps needed to move from current point to next point
        if dx < 0 and dy == 0:
          for step in range(abs(dx) + 1):
            matrix[x1 - step - min_x, y1 - min_y] = 10

        # Move down
        if dx > 0 and dy == 0:
          for step in range(dx + 1):                       
            matrix[x1 + step - min_x, y1 - min_y] = 10

        # Move right
        if dx == 0 and dy > 0:
          for step in range(dy + 1):
            matrix[x1 - min_x, y1 + step - min_y] = 10

        # Move left
        if dx == 0 and dy < 0:
          for step in range(abs(dy) + 1):
            matrix[x1 - min_x, y1 - step - min_y] = 10

        # Move up right
        if dx < 0 and dy > 0:
          for step in range(dy + 1):                       
            matrix[x1 - step - min_x, y1 + step - min_y] = 10

        # Move up left
        if dx < 0 and dy < 0:
          for step in range(abs(dy) + 1):
            matrix[x1 - step - min_x, y1 - step - min_y] = 10

        # Move down right
        if dx > 0 and dy > 0:
          for step in range(dx + 1):
            matrix[x1 + step - min_x, y1 + step - min_y] = 10

        # Move down left
        if dx > 0 and dy < 0:
          for step in range(dx + 1):
            matrix[x1 + step - min_x, y1 - step - min_y] = 10

    ImageMatrix.__init__(self, matrix, (min_x, min_y))
    fill.apply(self)
    self.kind = 'Polyline'
    self.fill = fill
    self.points = points

