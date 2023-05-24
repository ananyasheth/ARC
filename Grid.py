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
    return(self.group_of_shapes==self.original_image_matrix)