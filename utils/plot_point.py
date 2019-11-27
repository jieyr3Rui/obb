import numpy as np

check = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]

def get_point_3d(p, L, W, H, x, y, z):
    point = np.zeros([3, 8])
    for jj in range(8):
        point[:, jj] = check[jj][0] * L/2 * p[:, 0] + check[jj][1] * W/2 * p[:, 1] + check[jj][2] * H/2 * p[:, 2]
    point[0] += x
    point[1] += y
    point[2] += z
    return point

def plot_point_3d(ax, point):
    for ii in range(0,8):
        for jj in range(ii+1,8):
            c = 0
            for kk in range(3):
                c += (check[ii][kk] != check[jj][kk])
            if c == 1:
                l_plot = np.linspace(point[:, ii], point[:, jj], num = 50)
                ax.plot(l_plot[: ,0], l_plot[: ,1], l_plot[: ,2], c='r')