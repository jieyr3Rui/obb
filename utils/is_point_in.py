import numpy as np
 
# 判断该点是否在该条线上
 
# point:点坐标,如:[113.775698, 30.236892]
# o : 该条线的起点
# d : 该条线的终点
def is_point_in_line(point, o, d):
    # 先判断该点是否在线段范围内,如果不在,
    # 则就算在该方程的直线上但也不在该线段上
    if o[1] > point[1] and d[1] > point[1]:  # 该点纵坐标小于线段最小纵坐标
        return False
    if o[1] < point[1] and d[1] < point[1]:  # 该点纵坐标大于线段最大纵坐标
        return False
    if o[0] > point[0] and d[0] > point[0]:  # 该点横坐标小于线段最小横坐标
        return False
    if o[0] < point[0] and d[0] < point[0]:  # 该点横坐标大于线段最大横坐标
        return False
 
    # 若线段为垂直直线,则该点的横坐标等于该线段的横坐标才说明在该线段上
    if o[0] == d[0]:
        return True if point[0] == o[0] else False
 
    # 通过输入的两个点计算一元一次方程,通过输入x,计算y
    a = (d[1] - o[1]) / (d[0] - o[0])
    b = (d[0] * o[1] - o[0] * d[1]) / (d[0] - o[0])
    y = a * point[0] + b
    return True if y == point[1] else False
 
 
# 假设以该点向右水平做射线,判断该点是否与该线段有交点(只要线段与射线相交则为true)
# point:点坐标,如:[113.775698, 30.236892]
# o : 该条线的起点
# d : 该条线的终点
def is_ray_intersects_segment(point, o, d):
    if o[1] == d[1]:  # 如果线段是水平直线,则直接无交点
        return False
    # 先判断该点是否在线段范围内,如果不在,
    # 则就算在该方程的直线上但也不在该线段上
    if o[1] > point[1] and d[1] > point[1]:  # 该点纵坐标小于等于线段最小纵坐标
        return False
    if o[1] < point[1] and d[1] < point[1]:  # 该点纵坐标大于等于线段最大纵坐标
        return False
 
    # 先求出一元一次方程求交点
    # 若线段为垂直直线,则该点的横坐标应该小于该点的横坐标才能有交点
    # if o[0] == d[0]:
    #     return True if point[0] < o[0] else False
    #
    # # 通过输入的两个点计算一元一次方程,通过输入x,计算y
    # a = (d[1] - o[1]) / (d[0] - o[0])
    # b = (d[0] * o[1] - o[0] * d[1]) / (d[0] - o[0])
    # x = (point[1] - b) / a
 
    # 利用三角形比例关系求交点
    x = d[0] - (d[0] - o[0]) * (d[1] - point[1]) / (d[1] - o[1])
 
    # 如果该点的横坐标小于相同水平线上交点的横坐标,则有交点
    return True if point[0] < x else False
 
 
"""
判断是否在矩形区域内
point_coord:点坐标,如:[113.775698, 30.236892]
polygon_coords:封闭多边形,如:[[[113.76708006000003,30.231097985000019],
[113.77808006000006,30.231097985000019],[113.76708006000003,30.231097985000019]]]
is_contains_edge: 是否包含边界,如果为true,那么在边界上时也算在多边形内
"""
 
 
def is_point_in_polygon(point_coord, polygon_coords, is_contains_edge):
    intersect_count = 0  # 交点个数
    for polygon in polygon_coords:
        polygon = polygon.T
        # 循环每条边
        for i in range(len(polygon) - 1):
            origin_point = polygon[i]
            destination_point = polygon[i + 1]
 
            # 是否包含存在直线上的点
            if is_point_in_line(point_coord, origin_point, destination_point):
                return True if is_contains_edge else False
 
            if is_ray_intersects_segment(point_coord, origin_point, destination_point):
                # 有交点就加1
                intersect_count += 1
 
    # 如果恰好与端点相交,则查看相应的端点,并减去与该点相同纵坐标且在该点右侧的点的个数
    endpoint_intersects_count = 0
    for polygon in polygon_coords:
        # 遍历每一个点,但是因为最后一个点和第一个点是重复的,所以最后一个不遍历
        for i in polygon[:-1]:
            if i[1] == point_coord[1] and i[0] > point_coord[0]:
                endpoint_intersects_count += 1
    intersect_count -= endpoint_intersects_count
    return True if intersect_count % 2 == 1 else False
 
 
# poly = [[
#     [2.0, 4.0],
#     [2.0, 6.0],
#     [4.0, 8.0],
#     [6.0, 8.0],
#     [8.0, 6.0],
#     [8.0, 4.0],
#     [6.0, 2.0],
#     [4.0, 2.0],
#     [2.0, 4.0]
# ],
#     # [
#     #     [3.0, 5.0],
#     #     [4.0, 7.0],
#     #     [6.0, 7.0],
#     #     [7.0, 6.0],
#     #     [6.0, 5.0],
#     #     [3.0, 5.0]
#     # ]
# ]

# poi = np.array([1, 0])
# print(poi)
# poly = np.array([[[2, 2, 4, 6, 8, 8, 6, 4, 2],
#                  [4, 6, 8, 8, 6, 4, 2, 2, 4]]])
# print(poly[0].T)
# print(is_point_in_polygon(poi, poly, False))