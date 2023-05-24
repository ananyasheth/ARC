class Pair:
  '''
  The Pair class represents an ARC pair. 

  Attributes
  ----------
  input_grid : Grid object
    The input grid for this ARC pair.
  output_grid : Grid object
    The output grid for this ARC pair.

  Methods
  -------
  self.check_shapes()
    Prints the results of input_grid.check_shapes() and 
    output_grid.check_shapes().

  '''

  def __init__(self,input_grid,output_grid):
    self.input_grid = input_grid
    self.output_grid = output_grid

  def check_shapes(self):
    print('  input_grid',self.input_grid.check_shapes())
    print('  output_grid',self.output_grid.check_shapes())