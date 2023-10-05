import numpy as np

class ImageMatrix:
  '''
  The ImageMatrix class represents a matrix of colours, similar to the matrices 
  used to describe Grids in the original corpus. This class has three defining 
  attributes: matrix, x_offset, and y_offset. The matrix attribute stores the 
  actual matrix of colours. The x_offset and y_offset attributes give the 
  coordinates of the first element in the matrix. For example, a single dot at 
  x=5, y=3 with colour 9 would have the following attributes:
     matrix = np.array([[9]])
     x_offset = 5
     y_offset = 3
  
  Attributes
  ----------
  matrix : numpy array
    A two-dimensional numpy array. Each element in the array contains one of the
    following:
        - an integer from 0 to 9: corresponds to one of the colours in the
          original corpus
        - -1: corresponds to transparency
        - 10: corresponds to undefined
  x_offset : int
    The x coordinate of the first element in the matrix.
  y_offset : int
    The y coordinate of the first element in the matrix.
  min_x : int
    The x coordinate of the first element in the matrix (equal to x_offset).
  min_y : int
    The y coordinate of the first element in the matrix (equal to y_offset).
  max_x : int
    The x coordinate of the last element in the matrix.
  max_y : int
    The y coordinate of the last element in the matrix.
  
  Methods
  -------
  updateMatrix(matrix,x_offset=0,y_offset=0)
    Updates the object with a new matrix and offsets.
  self.getCell(x,y)
    Returns the value for cell x,y.
  self.updateCell(x,y,newValue)
    Changes the value for cell x,y to newValue.
  self.add_on_top(matrix_to_add)
    Adds another matrix on top of itself.
  self.delete(matrix_to_delete)
    Cuts a whole in itself using the shape of another matrix.
  self.split(row,column)
    Splits a matrix into two parts using the row or column number.

  '''

  def __init__(self,matrix,offset=(0,0)):
    self.updateMatrix(matrix,offset)

  def croppedMatrix(self,coords):
    ((x1,y1),(x2,y2)) = coords
    self.cropped_matrix=self.matrix[x1-(self.x_offset):x2-(self.x_offset)+1,y1-(self.y_offset):y2-(self.y_offset)+1]

  def updateMatrix(self,matrix,offset=(0,0)):
    (x_offset,y_offset) = offset
    self.min_x = x_offset
    self.max_x = len(matrix)+x_offset-1
    self.min_y = y_offset
    self.max_y = len(matrix[0])+y_offset-1
    self.x_offset = x_offset
    self.y_offset = y_offset
    self.x_size = self.max_x-self.min_x+1
    self.y_size = self.max_y-self.min_y+1
    self.matrix = matrix

  def __eq__(self, other):
    if not(isinstance(other,ImageMatrix)):
      return(False)
    if self.x_offset!=other.x_offset or self.y_offset!=other.y_offset:
      return(False)
    return(np.array_equal(self.matrix,other.matrix))

  def getCell(self,x,y):
    if x<self.min_x or x>self.max_x or y<self.min_y or y>self.max_y:
      return(-1)
    else:
      return(self.matrix[x-self.x_offset,y-self.y_offset])

  def updateCell(self,x,y,newValue):
    self.matrix[x-self.x_offset,y-self.y_offset] = newValue

  def add_on_top(self,matrix_to_add):
    min_x = min([self.min_x,matrix_to_add.min_x])
    max_x = max([self.max_x,matrix_to_add.max_x])
    x_size = max_x-min_x+1
    min_y = min([self.min_y,matrix_to_add.min_y])
    max_y = max([self.max_y,matrix_to_add.max_y])
    y_size = max_y-min_y+1
    matrix = np.full((x_size,y_size),-1)
    for m in [self,matrix_to_add]:
      for x in range(min_x,max_x+1):
        for y in range(min_y,max_y+1):
          m_value = m.getCell(x,y)
          if m_value is None:
            pass
          if m_value in (0,1,2,3,4,5,6,7,8,9):
            matrix[x-min_x,y-min_y] = m_value
    self.updateMatrix(matrix,(min_x,min_y))

  def delete(self,matrix_to_delete):
    for x in range(self.min_x,self.max_x+1):
      for y in range(self.min_y,self.max_y+1):
        m_value = matrix_to_delete.getCell(x,y)
        if m_value==-1:
          pass
        if m_value in (0,1,2,3,4,5,6,7,8,9):
          self.matrix[x-self.min_x,y-self.min_y] = -1
    
  def move_by(self,x,y):
    offset=(self.x_offset+x,self.y_offset+y)
    matrix = self.matrix
    self.updateMatrix(matrix,offset)

  def updateColour(self,colour):
    for x in range(self.min_x,self.max_x+1):
      for y in range(self.min_y,self.max_y+1):
        self.matrix[x-self.x_offset,y-self.y_offset] = colour

  def move_to_edge (self, background_x, background_y, direction):
    #example task:a8c38be5
    direction_coords = {
        'top': (0, int(round(background_y / 2))),
        'bottom': (background_x - 1, int(round(background_y / 2))),
        'left': (int(round(background_x / 2)), 0),
        'right': (int(round(background_x / 2)), background_y - 1),
        'top-left': (0, 0),
        'top-right': (0, background_y - 1),
        'bottom-left': (background_x - 1, 0),
        'bottom-right': (background_x - 1, background_y - 1)
        }
    # Get the coordinates for the selected direction
    target_x, target_y = direction_coords.get(direction, (0, 0))

    if direction == 'top':
      move_x = target_x - self.min_x
      move_y = target_y - (self.min_y + (int(round((self.y_size)/2))-1))
    elif direction == 'bottom':
      move_x = target_x - self.max_x
      move_y = target_y - (self.min_y + (int(round((self.y_size)/2))-1))
    elif direction == 'right':
      move_x = target_x - (self.min_x + (int(round((self.x_size)/2))-1))
      move_y = target_y - self.max_y
    elif direction == 'left':
      move_x = target_x - (self.min_x + (int(round((self.x_size)/2))-1))
      move_y = target_y - self.min_y

    if direction == 'top-left':
      move_x = target_x - self.min_x
      move_y = target_y - self.min_y
    elif direction == 'top-right':
      move_x = target_x - self.min_x
      move_y = target_y - self.max_y
    elif direction == 'bottom-left':
      move_x = target_x - self.max_x
      move_y = target_y - self.min_y
    elif direction == 'bottom-right':
      move_x = target_x - self.max_x
      move_y = target_y - self.max_y
      
    self.move_by(move_x, move_y)


  def duplicate(self, x, y):
      # Example task: b190f7f5
      # Create a copy of the current matrix
      duplicated_matrix = np.copy(self.matrix)
      
      # Create a new ImageMatrix instance with the duplicated matrix and new coordinates
      duplicated_image = ImageMatrix(duplicated_matrix, (self.x_offset + x, self.y_offset + y))
      
      return(duplicated_image)
