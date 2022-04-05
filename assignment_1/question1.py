def safe_call(func, *args):
    variables = func.__annotations__
    variables_name = func.__annotations__.keys()
    # checks that the number of arguments is the same
    if len(args) != func.__code__.co_argcount:
        raise Exception('wrong number of arguments')

    # goes over all of the arguments in the function
    for i in range(0, func.__code__.co_argcount):
        # checks if the argument in function has a type
        if variables_name.__contains__(func.__code__.co_varnames[i]) is True:
            # checks if types match
            if type(args[i]) != variables[func.__code__.co_varnames[i]]:
                raise TypeError('bad type of')

    return func(*args)


def f(x: int, y, z: float):
    return x + y + z


if __name__ == '__main__':
    print(safe_call(f, 2, 2.3, 111.))
