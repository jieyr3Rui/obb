import numpy as np
 
def is_point_in_line(point, o, d, command='2d'):
    if command == '2d':
        if o[1] > point[1] and d[1] > point[1]:
            return False
        if o[1] < point[1] and d[1] < point[1]:
            return False
        if o[0] > point[0] and d[0] > point[0]:
            return False
        if o[0] < point[0] and d[0] < point[0]:
            return False
    
        if o[0] == d[0]:
            return True if point[0] == o[0] else False
    

        a = (d[1] - o[1]) / (d[0] - o[0])
        b = (d[0] * o[1] - o[0] * d[1]) / (d[0] - o[0])
        y = a * point[0] + b
        return True if y == point[1] else False
    if command == '1d':
        return True if ((point > o) & point < d) else False
    return False
 
def is_ray_intersects_segment(point, o, d):
    if o[1] == d[1]:
        return False
    if o[1] > point[1] and d[1] > point[1]:
        return False
    if o[1] < point[1] and d[1] < point[1]:
        return False
 
    x = d[0] - (d[0] - o[0]) * (d[1] - point[1]) / (d[1] - o[1])
 
    return True if point[0] < x else False
 

def is_point_in_polygon(point_coord, polygon_coords, is_contains_edge):
    intersect_count = 0 
    for polygon in polygon_coords:
        polygon = polygon.T
        for i in range(len(polygon) - 1):
            origin_point = polygon[i]
            destination_point = polygon[i + 1]
 
            if is_point_in_line(point_coord, origin_point, destination_point):
                return True if is_contains_edge else False
 
            if is_ray_intersects_segment(point_coord, origin_point, destination_point):
                intersect_count += 1
 
    endpoint_intersects_count = 0
    for polygon in polygon_coords:
        for i in polygon[:-1]:
            if i[1] == point_coord[1] and i[0] > point_coord[0]:
                endpoint_intersects_count += 1
    intersect_count -= endpoint_intersects_count
    return True if intersect_count % 2 == 1 else False
