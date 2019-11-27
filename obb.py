import matplotlib.pyplot as plt
import numpy as np
from numpy import math
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_point import plot_point_3d, get_point_3d

ax = plt.figure().add_subplot(111, projection = '3d')


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
        ax.scatter(axises[0], axises[1],axises[2], c = color)

        x_ = np.sum(axises[0]) / n
        y_ = np.sum(axises[1]) / n
        z_ = np.sum(axises[2]) / n
        # print([x_, y_, z_])
        cov = np.cov(axises)
        # print(cov)
        val, p = np.linalg.eig(cov)
        # print(val,'\n', p)

        # axises_new = np.dot(axises.T, p).T
        axises_p = np.dot(p.T, axises)
        # print(axises_new)
        # max_index, max_number = max(enumerate(x), key=operator.itemgetter(1))
        _, __, L_ = get_len(axises_p, 0)
        _, __, W_ = get_len(axises_p, 1)
        _, __, H_ = get_len(axises_p, 2)
        point = get_point_3d( p, L_, W_, H_, x_, y_, z_)
        plot_point_3d(ax, point)

        self.point = point
        self.pos = np.array([x_, y_, z_])
        self.sha = np.array([L_, W_, H_])
        self.p = p
        self.axises = axises
        
        

o1 = OBB(1,2,3,  0.7,0.3,-0.1, 2,2,2, 100, 'b')
o2 = OBB(-2,0,-3, 1.2,-0.1,0.7, 3,1,3, 100, 'g')

# print(np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T )
ax1 = plt.figure().add_subplot(111, projection = '3d')
point_in_o1 = o2.point -  np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T 
axises_p1 = np.dot(o1.p.T, point_in_o1)
plot_point_3d(ax1, axises_p1)
point_in_o1 = o1.point -  np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T 
axises_p1 = np.dot(o1.p.T, point_in_o1)
plot_point_3d(ax1, axises_p1)


plt.show()


