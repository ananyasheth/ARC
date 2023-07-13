import numpy as np

class Grid:
  '''
  The Grid class represents an ARC grid. 
  
  Attributes
  ----------
  original_image_matrix : ImageMatrix object
    In the original corpus, a Grid is stored as a matrix. This attribute stores
    that original matrix as an ImageMatrix object.
  group_of_shapes : GroupOfShapes object
    A group of shapes that provides a precise definition of the grid using the
    Shape subclasses.
  
  Methods
  -------
  self.check_shapes()
    Returns None if group_of_shapes is None. 
    Returns True if group_of_shapes.image_matrix is equal to original_image_matrix. 
    Returns False otherwise.
  
  '''

  def __init__(self,original_image_matrix,group_of_shapes=None):
    self.original_image_matrix = original_image_matrix
    self.group_of_shapes = group_of_shapes

  def check_shapes(self):
    if self.group_of_shapes is None:
      return(None)
    background_coords = ((self.group_of_shapes.shapes[0].min_x,self.group_of_shapes.shapes[0].min_y),(self.group_of_shapes.shapes[0].max_x,self.group_of_shapes.shapes[0].max_y))
    self.group_of_shapes.croppedMatrix(background_coords)
    return(np.array_equal(self.group_of_shapes.cropped_matrix,self.original_image_matrix.matrix))
