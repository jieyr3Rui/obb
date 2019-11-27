import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_shape import plot_shape_3d, get_point_3d
from box import box_3d

def obb_3d_check_face(o1, o2):
    pos = np.array((o1.pos + o2.pos) / 2)

    o2_point_in_o1 = np.dot(o1.p.T, o2.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)
    o1_point_in_o1 = np.dot(o1.p.T, o1.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)
    # ax = plt.figure().add_subplot(111, projection = '3d')
    # plot_shape_3d(ax, o1_point_in_o1, 'r')
    # plot_shape_3d(ax, o2_point_in_o1, 'r')
    # plt.show()

    o1_pi_point_in_o1 = np.zeros_like(o1_point_in_o1)
    o2_pi_point_in_o1 = np.zeros_like(o2_point_in_o1)
    o1_pi_point_in_word = np.zeros_like(o1.point)
    o2_pi_point_in_word = np.zeros_like(o2.point)

    for face in range(3):
        for ii in range(3):
            if ii == face:
                o1_pi_point_in_o1[ii] = 0
                o2_pi_point_in_o1[ii] = 0
            else:
                o1_pi_point_in_o1[ii] = o1_point_in_o1[ii]
                o2_pi_point_in_o1[ii] = o2_point_in_o1[ii]
        
        o1_pi_point_in_word = np.dot(o1.p, o1_pi_point_in_o1) + np.array(np.tile(pos,(1,8)).reshape([8,3])).T
        o2_pi_point_in_word = np.dot(o1.p, o2_pi_point_in_o1) + np.array(np.tile(pos,(1,8)).reshape([8,3])).T
        ax = plt.figure().add_subplot(111, projection = '3d')
        o1.plot_shape(ax, 'r')
        o2.plot_shape(ax, 'g')
        plot_shape_3d(ax, o1_pi_point_in_word, 'b')
        plot_shape_3d(ax, o2_pi_point_in_word, 'y')
        plt.show()

    
    return

def obb_3d_check(o1, o2):
    # face
    obb_3d_check_face(o1, o2)

    return