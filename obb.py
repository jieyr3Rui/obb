import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_point import plot_shape_3d, get_point_3d
from box import box_3d

def obb_3d_check(o1, o2):


    # print(np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T )
    ax1 = plt.figure().add_subplot(111, projection = '3d')
    point_in_o1 = o2.point -  np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T 
    axises_p1 = np.dot(o1.p.T, point_in_o1)
    plot_shape_3d(ax1, axises_p1, 'r')
    point_in_o1 = o1.point -  np.array(np.tile(o1.pos,(1,8)).reshape([8,3])).T 
    axises_p1 = np.dot(o1.p.T, point_in_o1)
    plot_shape_3d(ax1, axises_p1, 'r')


    plt.show()