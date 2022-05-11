import math

from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np


def plotIntersection(space, f, g):
    point_set: set = set()
    for i in range(math.ceil(space.min()), math.ceil(space.max())):
        x = fsolve(lambda x: f(x) - g(x), i)[0]
        if round(f(x), 3) == round(g(x), 3) and space.min()<=x<=space.max():
            point_set.add(x)
    arr = np.array([[x, f(x)] for x in point_set])
    plt.grid()
    plt.scatter(arr[:, 0], arr[:, 1], c= 'red', alpha=1)
    plt.plot(space, f(space))
    plt.plot(space, g(space))
    plt.show()


if __name__ == '__main__':
    f1 = lambda x: x ** 2
    g1 = lambda x: x + 10
    f2 = lambda x: np.sin(x)
    g2 = lambda x: 0.2 * x
    f3 = lambda x: np.cos(x)
    g3 = lambda x: x+9
    plt_space = np.linspace(-10, 10, 1000)
    plotIntersection(plt_space, f1, g1)
    plotIntersection(plt_space, f2, g2)
    plotIntersection(plt_space, f3, g3)
    plotIntersection(np.linspace(-8, 4, 1000), f3, f2)

