import numpy as np
from utils.convex_hull import convex_hull
from utils.is_point_in import is_point_in_polygon

def check_intersect_polygon(p1, p2):
    sha1 = p1.shape[1]
    sha2 = p2.shape[1]
    p = np.zeros([2, sha1*sha2])
    for ii in range(sha1):
        for jj in range(sha2):
            p[:, ii*sha2 + jj] = p1[:, ii] - p2[:, jj]
    
    p = convex_hull(p)
    poly = np.zeros([1, 2, p.shape[1]])
    poly[0] = p
    
    return p, is_point_in_polygon(np.array([0,0]), poly, False)

def check_intersect_line(line1, line2, color1='orange', color2='green', color_in='purple', color_out='w'):
    line = np.zeros(4)
    attr = []
    is_intersect = True

    # line1      *----*
    # line2  *------*
    if   ((line1[0] <= line2[1]) & (line1[0] >= line2[0])) & (line1[1] >= line2[1]):
        line = np.array([line2[0], line1[0], line2[1], line1[1]])
        attr = [color2, color_in, color1]
        is_intersect = True

    # line1  *----*
    # line2    *------*
    elif ((line2[0] <= line1[1]) & (line2[0] >= line1[0])) & (line2[1] >= line1[1]):
        line = np.array([line1[0], line2[0], line1[1], line2[1]])
        attr = [color1, color_in, color2]
        is_intersect = True

    # line1  *-----------*
    # line2    *------*
    elif (line1[0] <= line2[0]) & (line1[1] >= line2[1]):
        line = np.array([line1[0], line2[0], line2[1], line1[1]])
        attr = [color1, color_in, color1]
        is_intersect = True

    # line1     *-----*
    # line2  *-----------*
    elif (line2[0] <= line1[0]) & (line2[1] >= line1[1]):
        line = np.array([line2[0], line1[0], line1[1], line2[1]])
        attr = [color2, color_in, color2]
        is_intersect = True

    # line1             *-----*
    # line2  *------*
    elif (line1[0] >= line2[1]):
        line = np.array([line2[0], line2[1], line1[0], line1[1]])
        attr = [color2, color_out, color1]
        is_intersect = False

    # line1   *-----*
    # line2            *------*
    elif (line2[0] >= line1[1]):
        line = np.array([line1[0], line1[1], line2[0], line2[1]])
        attr = [color1, color_out, color2]
        is_intersect = False

    return line, attr, is_intersect