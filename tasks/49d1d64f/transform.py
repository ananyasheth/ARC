from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    dots = group_of_shapes.fetch_shape(kind=['Dot'])
    background = group_of_shapes.fetch_shape(kind=['Background'])[0]

    # Background size add one more outer layer
    new_background = Background((background.x_size+2, background.y_size+2))
    new_group_of_shapes.append(new_background)

    for dot in dots:
        if  dot.check_corner((background.x_size,background.y_size)) == 'top-left':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'top',dot.fill.colour))
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'left',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'top-right':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'top',dot.fill.colour))
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'right',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'bottom-left':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'bottom',dot.fill.colour))
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'left',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'bottom-right':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'bottom',dot.fill.colour))
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'right',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'top':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'top',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'bottom':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'bottom',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'left':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'left',dot.fill.colour))
        elif dot.check_corner((background.x_size,background.y_size)) == 'right':
            dot.move_by(1,1)
            new_group_of_shapes.append(group_of_shapes.extend((9,9),(dot.min_x,dot.min_y),'right',dot.fill.colour))
        else:
            dot.move_by(1,1)
        new_group_of_shapes.append(dot)
    return GroupOfShapes(new_group_of_shapes)
