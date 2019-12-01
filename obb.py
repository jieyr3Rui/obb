import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from utils.rotate import rotate
from utils.get_len import get_len
from utils.plot_shape import plot_shape_3d, plot_poly, plot_line
from utils.convex_hull import convex_hull
from utils.check_intersect import check_intersect_polygon, check_intersect_line
from box import box_3d

def obb_3d_check_face(o1, o2):
    plt.figure(figsize=[15, 10])
    pos = np.array((o1.pos + o2.pos) / 2)

    o2_point_in_o1 = np.dot(o1.p.T, o2.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)
    o1_point_in_o1 = np.dot(o1.p.T, o1.point -  np.array(np.tile(pos,(1,8)).reshape([8,3])).T)

    for face in range(3):
        jj = 0
        o1_poly_input = np.zeros([2, o1_point_in_o1.shape[1]])
        o2_poly_input = np.zeros([2, o2_point_in_o1.shape[1]])
        for ii in range(3):
            if ii != face:
                o1_poly_input[jj] = o1_point_in_o1[ii]
                o2_poly_input[jj] = o2_point_in_o1[ii]
                jj += 1
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
        poly_gjk, result = check_intersect_polygon(o1_poly_in_o1, o2_poly_in_o1)
        check = 'true' if result == True else 'false'

        
        ax = plt.subplot(2,3,(face+1), projection = '3d')
        o1.plot_shape(ax, 'r')
        o2.plot_shape(ax, 'g')
        o1.plot_scatter(ax, 'r')
        o2.plot_scatter(ax, 'g')
        plot_poly(ax, o1_poly_in_word, 'b', d='3d')
        plot_poly(ax, o2_poly_in_word, 'y', d='3d')
        ax = plt.subplot(2,3,(face+4))
        plot_poly(ax, o1_poly_in_o1, 'b', d='2d')
        plot_poly(ax, o2_poly_in_o1, 'y', d='2d')
        plot_poly(ax, poly_gjk,      'r', d='2d')
        plt.title('polygon check reslut: ' +  check)
        plt.grid()
    
    plt.show()

    
    return

def obb_3d_check_line(o1, o2):
    plt.figure(figsize=[10, 10])
    pos = np.array((o1.pos + o2.pos)/2)
    for ii in range(3):
        for jj in range(3):

            p = o1.p.T[ii] * o2.p.T[jj]
            # norm
            p = p / np.linalg.norm(p)
            _, line1_in_p, __ = get_len(np.dot(p, o1.point - np.array(np.tile(pos,(1,8)).reshape([8,3])).T))
            _, line2_in_p, __ = get_len(np.dot(p, o2.point - np.array(np.tile(pos,(1,8)).reshape([8,3])).T))
            line_in_p, attr, is_intersect = check_intersect_line(line1_in_p, line2_in_p)
            line_in_world = np.zeros([line_in_p.shape[0], 3])
            for kk in range(line_in_p.shape[0]):
                line_in_world[kk] = line_in_p[kk] * p + pos
            line_in_world = line_in_world.T

            ax = plt.subplot(3,3,(3*ii+jj+1), projection = '3d')
            o1.plot_shape(ax, 'r')
            o2.plot_shape(ax, 'b')
            plot_line(ax, line_in_world[:, 0], line_in_world[:,1], attr[0])
            plot_line(ax, line_in_world[:, 1], line_in_world[:,2], attr[1])
            plot_line(ax, line_in_world[:, 2], line_in_world[:,3], attr[2])
    plt.show()


    return

def obb_3d_check(o1, o2):
    # face
    
    obb_3d_check_face(o1, o2)
    obb_3d_check_face(o2, o1)
    obb_3d_check_line(o1, o2)
    return