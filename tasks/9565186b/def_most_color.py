from ImageMatrix import *
from Shape import *
from Fill import *

class GroupOfShapes(Shape):
  


    def most_color_shape(self, kind):
        color_count_dict = {}
        most_color_shape = None
        max_count = 0

        for shape in self.shapes:
            color = shape.fill
            if color in color_count_dict:
                color_count += 1
            else:
                color_count = 1

            if color_count_dict[color] > max_count:
                max_count = color_count_dict[color]
                most_color_shape = shape
        
        return most_color_shape
