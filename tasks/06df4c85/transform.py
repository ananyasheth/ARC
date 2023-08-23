from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes=[group_of_shapes]
    number_of_dots=[]
    background = group_of_shapes.fetch_shape(['Background'])[0]
    lines = group_of_shapes.fetch_shape(['HLine','VLine'])
    dots = group_of_shapes.fetch_shape(['Dot'])
    intersection_points = group_of_shapes.intersection_of_lines(lines)
    segments = group_of_shapes.segment_grid(intersection_points,2)
    list_of_rectangle = []
    

    rectangles = group_of_shapes.fetch_shape(['Rectangle'])
    
    for index,current_rectangle in enumerate(rectangles):
        for next_index in range(index + 1, len(rectangles)):
            next_rectangle = rectangles[next_index]
            if next_rectangle.fill.colour == current_rectangle.fill.colour and next_rectangle.min_x == current_rectangle.min_x:
                lowerbound_corr_x= current_rectangle.min_x
                upperbound_corr_x=current_rectangle.max_x
                lowerbound_corr_y=current_rectangle.max_y
                upperbound_corr_y=next_rectangle.min_y

                for each_segment in segments:
                    if each_segment[0][0] == current_rectangle.min_x and each_segment[0][1] > lowerbound_corr_y and each_segment[0][1] < upperbound_corr_y:
                        new_group_of_shapes.append(Rectangle(each_segment,SolidFill(current_rectangle.fill.colour)))

            elif next_rectangle.fill.colour == current_rectangle.fill.colour and next_rectangle.min_y == current_rectangle.min_y:
                lowerbound_corr_x= current_rectangle.max_x
                upperbound_corr_x= next_rectangle.min_x
                lowerbound_corr_y= current_rectangle.min_y
                upperbound_corr_y= current_rectangle.min_y

                for each_segment in segments:
                    if each_segment[0][1] == current_rectangle.min_y and each_segment[0][0] > lowerbound_corr_x and each_segment[0][0] < upperbound_corr_x:
                        new_group_of_shapes.append(Rectangle(each_segment,SolidFill(current_rectangle.fill.colour)))                        

    return (GroupOfShapes(new_group_of_shapes))

