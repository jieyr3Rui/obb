import math
import numpy as np
from utils.check_point_in import is_point_in_polygon

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

def get_leftbottompoint(p):
    k = 0
    for i in range(1, len(p)):
        if p[i][1] < p[k][1] or (p[i][1] == p[k][1] and p[i][0] < p[k][0]):
            k = i
    return k

def multiply(p1, p2, p0):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

def get_arc(p1, p0):
    if (p1[0] - p0[0]) == 0:
        if ((p1[1] - p0[1])) == 0:
            return -1
        else:
            return math.pi / 2
    tan = float((p1[1] - p0[1])) / float((p1[0] - p0[0]))
    arc = math.atan(tan)
    if arc >= 0:
        return arc
    else:
        return math.pi + arc

def sort_points_tan(p, pk):
    p2 = []
    for i in range(0, len(p)):
        p2.append({"index": i, "arc": get_arc(p[i], pk)})

    p2.sort(key=lambda k: (k.get('arc')))

    p_out = []
    for i in range(0, len(p2)):
        p_out.append(p[p2[i]["index"]])
    return p_out

def convex_hull(point):
    # input  [[x1, x2, x3], 
    #        [y1, y2, y3]]
    # need   [[x1, y1],
    #         [x2, y2],
    #         [x3, y3]]
    point = point.T
    # transform to list[tuple]
    p = []
    for ii in range(point.shape[0]):
        p.append(tuple(totuple(i) for i in point[ii]))
    p=list(set(p))
    k = get_leftbottompoint(p)
    pk = p[k]
    p.remove(p[k])

    p_sort = sort_points_tan(p, pk)

    p_result = [pk,p_sort[0]]

    top = 2
    for i in range(1, len(p_sort)):
        while(multiply(p_result[-2], p_sort[i],p_result[-1]) > 0):
            p_result.pop()
        p_result.append(p_sort[i])
    # output [[x1, x2, x3],
    #         [y1, y2, y3]]
    return np.array(p_result).T

def polygon_check(p1, p2):
    sha1 = p1.shape[1]
    sha2 = p2.shape[1]
    p = np.zeros([2, sha1*sha2])
    #print('sha: ',sha1, sha2)
    for ii in range(sha1):
        for jj in range(sha2):
            #print('ii jj = ', ii, jj)
            #print(ii*sha1 + jj)
            p[:, ii*sha2 + jj] = p1[:, ii] - p2[:, jj]
    
    poly = np.zeros([1, 2, sha1 * sha2])
    poly[0] = p
    
    return is_point_in_polygon(np.array([0,0]), poly, False)