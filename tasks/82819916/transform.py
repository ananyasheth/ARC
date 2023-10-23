from ImageMatrix import *
from Shape import *
from Fill import *
from GroupOfShapes import *

def transform(group_of_shapes):
    new_group_of_shapes = []
    new_group_of_shapes.append(group_of_shapes.fetch_shape(kind=['Background'])[0])
    gos_list = group_of_shapes.fetch_shape(kind=['GroupOfShapes'])
    benchmark_shape = gos_list[0]
    benchmark_dots = benchmark_shape.fetch_shape(kind=['Dot'])
    for benchmark_dot in benchmark_dots:
        new_group_of_shapes.append(benchmark_dot)
    
    # create dictionary for colour mapping
    shape_dict = {}     # Outer dictionary
    for index, gos in enumerate(gos_list[1:]):
        extend_dots = gos.fetch_shape(kind=['Dot'])
        colour_dict = {}    # inner dictionary
        for extend_dot in extend_dots:
            for benchmark_dot in benchmark_dots[0:(len(extend_dots))]:
                if benchmark_dot.min_y == extend_dot.min_y:
                    colour_dict[benchmark_dot.fill.colour] = extend_dot.fill.colour
        shape_dict[index] = colour_dict

    # new dots
    for index, gos in enumerate(gos_list[1:]):
        extend_dot = gos.fetch_shape(kind=['Dot'])[0]
        for benchmark_dot in benchmark_dots:
            new_group_of_shapes.append(Dot((extend_dot.min_x, benchmark_dot.min_y),SolidFill(shape_dict[index][benchmark_dot.fill.colour])))
            
            
    return (GroupOfShapes(new_group_of_shapes))
