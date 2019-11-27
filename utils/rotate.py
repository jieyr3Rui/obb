import numpy as np
from numpy import math

def rotate(pitch, roll, yaw):
    p = np.array([[ 1,                 0,                0],
                  [ 0,   math.cos(pitch), -math.sin(pitch)],
                  [ 0,   math.sin(pitch),  math.cos(pitch)]])

    r = np.array([[ math.cos(roll),    0,  math.sin(roll)],
                  [ 0,                 1,  0             ],
                  [-math.sin(roll),    0,  math.cos(roll)]])

    y = np.array([[ math.cos(yaw), -math.sin(yaw), 0],
                  [ math.sin(yaw),  math.cos(yaw), 0],
                  [ 0,                          0, 1]])
    ro = np.dot(p, np.dot(r, y))
    return ro