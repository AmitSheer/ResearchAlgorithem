import math

from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np


def plotIntersection(space, f, g):
    point_set: set = set()
    for i in range(math.ceil(space.min()), math.ceil(space.max())):
        x = fsolve(lambda x: f(x) - g(x), i)[0]
        if round(f(x), 3) == round(g(x), 3):
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
    plt_space = np.linspace(-10, 10, 1000)
    # plt.grid()
    # plt.plot(plt_space, f1(plt_space))
    # plt.plot(plt_space, g1(plt_space))
    # plt.show()
    plotIntersection(plt_space, f1, g1)
    plotIntersection(plt_space, f2, g2)
