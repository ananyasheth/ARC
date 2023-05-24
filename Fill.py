import numpy as np
from ImageMatrix import *

class Fill:
  pass

class SolidFill(Fill):

  def __init__(self,colour):
    self.colour = colour
    self.kind = 'SolidFill'

  def apply(self,matrix):
    for x in range(matrix.min_x,matrix.max_x+1):
      for y in range(matrix.min_y,matrix.max_y+1):
        if  matrix.getCell(x,y)>-1:
          matrix.updateCell(x,y,self.colour)

class CheckeredFill(Fill):

  def __init__(self,colours):
    self.colours = colours
    self.kind = 'CheckeredFill'

  def apply(self,matrix):
    for x in range(matrix.min_x,matrix.max_x+1):
      colour_n = 0
      for y in range(matrix.min_y,matrix.max_y+1):
        if  matrix.getCell(x,y)>-1:
          matrix.updateCell(x,y,self.colours[colour_n])
          colour_n += 1
          if colour_n >= len(self.colours):
            colour_n = 0
