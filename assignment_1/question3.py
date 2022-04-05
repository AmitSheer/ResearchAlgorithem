def find_root(f, x1: float, x2: float) -> float:
    # variables for the function
    epsilon = 0.0000000001
    h = 0.0000000001
    # f_diff approximation of the Derivative of the given function
    f_diff = lambda x: float((f(x + h) - f(x)) / h)
    sqr_root = (x1 + x2) / 2
    new_eps = float(f(sqr_root) / f_diff(sqr_root))
    while new_eps >= epsilon and x1 <= sqr_root <= x2:
        sqr_root = sqr_root - new_eps
        new_eps = float(f(sqr_root) / f_diff(sqr_root))
    return sqr_root


if __name__ == '__main__':
    func = lambda x: x ** 2 - 4
    print(find_root(func, 2, 3))
