from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = [group_of_shapes]
    background = group_of_shapes.fetch_shape(['Background'])
    background = background[0]
    dot = group_of_shapes.fetch_shape(['Dot'])
    dot = dot[0]

    # Create a function to find the lastpoint of diagional line
    def find_last_point_of_diagonal(size, start_x, start_y, direction):
        x, y = start_x, start_y

        # Iterate to find the last point of the diagonal line based on the direction
        if direction == "top-left":
            while x > 0 and y > 0:
                x -= 1
                y -= 1
        elif direction == "top-right":
            while x > 0 and y < size - 1:
                x -= 1
                y += 1
        elif direction == "bottom-left":
            while x < size - 1 and y > 0:
                x += 1
                y -= 1
        elif direction == "bottom-right":
            while x < size - 1 and y < size - 1:
                x += 1
                y += 1
        return (x, y)

    top_left_point = find_last_point_of_diagonal(background.x_size, dot.min_x, dot.min_y, "top-left")
    top_right_point = find_last_point_of_diagonal(background.x_size, dot.min_x, dot.min_y, "top-right")
    bottom_left_point = find_last_point_of_diagonal(background.x_size, dot.min_x, dot.min_y, "bottom-left")
    bottom_right_point = find_last_point_of_diagonal(background.x_size, dot.min_x, dot.min_y, "bottom-right")

    line_1 = Line((top_left_point,bottom_right_point),SolidFill(dot.fill.colour))
    line_2 = Line((top_right_point ,bottom_left_point),SolidFill(dot.fill.colour))
    new_group_of_shapes.extend([line_1, line_2])

    return (GroupOfShapes(new_group_of_shapes))
