import matplotlib.pyplot as plt
import numpy as np
from numpy import math
from mpl_toolkits.mplot3d import Axes3D
import operator

ax = plt.figure().add_subplot(111, projection = '3d')

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

def get_len(axises_new, channel):
    _, max_ =  max(enumerate(axises_new[:, channel]), key=operator.itemgetter(1))
    _, min_ =  min(enumerate(axises_new[:, channel]), key=operator.itemgetter(1))
    return ((max_ - min_) / 2)

def plot_axis(p, L, W, H, x, y, z):
    axises = np.zeros([3, 8])
    check = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
    for jj in range(8):
        axises[:, jj] = check[jj][0] * L * p[:, 0] + check[jj][1] * W * p[:, 1] + check[jj][2] * H * p[:, 2]
    axises[0] += x
    axises[1] += y
    axises[2] += z
    for ii in range(0,8):
        for jj in range(ii+1,8):
            c = 0
            for kk in range(3):
                c += (check[ii][kk] != check[jj][kk])
            if c == 1:
                l_plot = np.linspace(axises[:, ii], axises[:, jj], num = 50)
                ax.plot(l_plot[: ,0], l_plot[: ,1], l_plot[: ,2], c='r')
    return 

class OBB():
    def __init__(self, x, y, z, pitch, roll, yaw, L, W, H, n, color):
        super().__init__()
        axises = np.random.rand(3, n)
        axises = (axises - 0.5)
        axises[0] *= L
        axises[1] *= W
        axises[2] *= H
        axises = np.dot(rotate(pitch, roll, yaw), axises)
        axises[0] += x
        axises[1] += y
        axises[2] += z
        self.axises = axises
        ax.scatter(axises[0], axises[1],axises[2], c = color)

        x_ = np.sum(axises[0]) / n
        y_ = np.sum(axises[1]) / n
        z_ = np.sum(axises[2]) / n
        # print([x_, y_, z_])
        cov = np.cov(axises)
        # print(cov)
        val, p = np.linalg.eig(cov)
        # print(val,'\n', p)
        
        axises_new = np.dot(axises.T, p)
        # print(axises_new)
        # max_index, max_number = max(enumerate(x), key=operator.itemgetter(1))
        L_ = get_len(axises_new, 0)
        W_ = get_len(axises_new, 1)
        H_ = get_len(axises_new, 2)

        # print(axises_new[:, 0])
        plot_axis(p, L_, W_, H_, x_, y_, z_)


        
        

o1 = OBB(1,2,3,  0.7,0.3,-0.1, 2,2,2, 100, 'b')
o2 = OBB(-2,0,-3, 1.2,-0.1,0.7, 3,1,3, 100, 'g')

plt.show()


