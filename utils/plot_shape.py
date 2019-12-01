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

def plot_shape_3d(ax, point, color):
    for ii in range(0,8):
        for jj in range(ii+1,8):
            c = 0
            for kk in range(3):
                c += (check[ii][kk] != check[jj][kk])
            if c == 1:
                l_plot = np.linspace(point[:, ii], point[:, jj], num = 50)
                ax.plot(l_plot[: ,0], l_plot[: ,1], l_plot[: ,2], c=color)
    return

def plot_poly(ax, point, color, d='3d'):
    if d == '3d':
        n = point.shape[1]
        for ii in range(n-1):
            l_plot = np.linspace(point[:, ii], point[:, ii+1], num=50)
            ax.plot(l_plot[: ,0], l_plot[: ,1], l_plot[: ,2], c=color)
        l_plot = np.linspace(point[:, n-1], point[:, 0], num = 50)
        ax.plot(l_plot[: ,0], l_plot[: ,1], l_plot[: ,2], c=color)
    if d == '2d':
        n = point.shape[1]
        for ii in range(n-1):
            l_plot = np.linspace(point[:, ii], point[:, ii+1], num = 50)
            ax.plot(l_plot[: ,0], l_plot[: ,1], c=color)
        l_plot = np.linspace(point[:, n-1], point[:, 0], num = 50)
        ax.plot(l_plot[: ,0], l_plot[: ,1], c=color)

def plot_line(ax, point1, point2, color, d='3d'):
    if d == '3d':
        line = np.linspace(point1, point2, num=50)
        ax.plot(line[:,0], line[:,1], line[:,2], c=color)
        return
    if d == '2d':
        x = np.linspace(point1, point1, num=50)
        y = np.zeros_like(x)
        ax.plot(x, y, c=color)
    return