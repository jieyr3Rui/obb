import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_point import plot_shape_3d, get_point_3d

class box_3d():
    def __init__(self):
        super().__init__()
        self.p = np.ones(3)
        self.sha = np.zeros(3)
        self.pos = np.zeros(3)
        self.point = np.zeros([3, 8])
        self.axises = np.zeros([3, 1])
    
    def update(self, p, sha, pos, point):
        self.p = p
        self.sha = sha
        self.pos = pos
        self.point = point
        return

    def get_by_axis(self, x, y, z, pitch, roll, yaw, L, W, H, n):
        self.axises = np.zeros([3, n])
        axises = np.random.rand(3, n)
        axises = (axises - 0.5)
        axises[0] *= L
        axises[1] *= W
        axises[2] *= H
        axises = np.dot(rotate(pitch, roll, yaw), axises)
        axises[0] += x
        axises[1] += y
        axises[2] += z

        x_ = np.sum(axises[0]) / n
        y_ = np.sum(axises[1]) / n
        z_ = np.sum(axises[2]) / n
        cov = np.cov(axises)
        val, p = np.linalg.eig(cov)
        axises_in_p = np.dot(p.T, axises)

        _, __, L_ = get_len(axises_in_p, 0)
        _, __, W_ = get_len(axises_in_p, 1)
        _, __, H_ = get_len(axises_in_p, 2)
        point = get_point_3d( p, L_, W_, H_, x_, y_, z_)
        
        self.update(p, [L_, W_, H_], [x_, y_, z_], point)
        self.axises = axises
        return 

    def get_by_point(self, point):
        return

    def get_by_param(self, p, sha, pos):
        return
    
    def plot_shape(self, ax, color):
        plot_shape_3d(ax, self.point, color)
        return

    def plot_scatter(self, ax, color):
        ax.scatter(self.axises[0], self.axises[1], self.axises[2], c = color)
        return
