import numpy as np
from utils.convex_hull import convex_hull
from utils.is_point_in import is_point_in_polygon

def check_intersect_polygon(p1, p2):
    sha1 = p1.shape[1]
    sha2 = p2.shape[1]
    p = np.zeros([2, sha1*sha2])
    #print('sha: ',sha1, sha2)
    for ii in range(sha1):
        for jj in range(sha2):
            #print('ii jj = ', ii, jj)
            #print(ii*sha1 + jj)
            p[:, ii*sha2 + jj] = p1[:, ii] - p2[:, jj]
    
    p = convex_hull(p)
    poly = np.zeros([1, 2, p.shape[1]])
    poly[0] = p
    
    return p, is_point_in_polygon(np.array([0,0]), poly, False)

def check_intersect_line():
    return