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
