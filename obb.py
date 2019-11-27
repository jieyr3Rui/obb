import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_shape import plot_shape_3d, plot_poly
from utils.polygon import convex_hull, polygon_check
from box import box_3d

def obb_3d_check_face(o1, o2):
    pos = np.array((o1.pos + o2.pos) / 2)

    o2_point_in_o1 = np.dot(o1.p.T, o2.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)
    o1_point_in_o1 = np.dot(o1.p.T, o1.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)
    # ax = plt.figure().add_subplot(111, projection = '3d')
    # plot_shape_3d(ax, o1_point_in_o1, 'r')
    # plot_shape_3d(ax, o2_point_in_o1, 'r')
    # plt.show()

    # o1_poly_point_in_o1 = np.zeros([3, 1])
    # o2_poly_point_in_o1 = np.zeros([3,1])
    # o1_poly_point_in_word = np.zeros([3,1])
    # o2_poly_point_in_word = np.zeros([3,1])

    
    for face in range(3):
        jj = 0
        o1_poly_input = np.zeros([2, o1_point_in_o1.shape[1]])
        o2_poly_input = np.zeros([2, o2_point_in_o1.shape[1]])
        for ii in range(3):
            if ii != face:
                o1_poly_input[jj] = o1_point_in_o1[ii]
                o2_poly_input[jj] = o2_point_in_o1[ii]
                jj += 1
        # print(o1_poly_input)
        o1_poly_in_o1 = convex_hull(o1_poly_input)
        o2_poly_in_o1 = convex_hull(o2_poly_input)

        sha1 = o1_poly_in_o1.shape[1]
        sha2 = o2_poly_in_o1.shape[1]

        o1_poly_in_word = np.zeros([3, sha1])
        o2_poly_in_word = np.zeros([3, sha2])

        jj = 0
        for ii in range(3):
            if ii != face:
                o1_poly_in_word[ii] = o1_poly_in_o1[jj]
                o2_poly_in_word[ii] = o2_poly_in_o1[jj]
                jj += 1
            else:
                o1_poly_in_word[ii] = 6
                o2_poly_in_word[ii] = 6

        o1_poly_in_word = np.dot(o1.p, o1_poly_in_word) + np.array(np.tile(pos,(1,sha1)).reshape([sha1,3])).T
        o2_poly_in_word = np.dot(o1.p, o2_poly_in_word) + np.array(np.tile(pos,(1,sha2)).reshape([sha2,3])).T
        

        ax = plt.figure().add_subplot(111, projection = '3d')
        o1.plot_shape(ax, 'r')
        o2.plot_shape(ax, 'g')
        plot_poly(ax, o1_poly_in_word, 'b')
        plot_poly(ax, o2_poly_in_word, 'y')
        plt.show()

    
    return

def obb_3d_check(o1, o2):
    # face
    obb_3d_check_face(o1, o2)
    obb_3d_check_face(o2, o1)
    return