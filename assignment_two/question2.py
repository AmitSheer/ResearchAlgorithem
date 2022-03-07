import functools

global m


class Memorise(object):
    def __init__(self):
        self.calls = {}

    def add_call(self, key, value):
        self.calls[key] = value

    def has_call(self, key):
        if self.calls.keys().__contains__(key):
            return self.calls[key]
        else:
            return None


def lastcall(func: callable):
    m = Memorise()

    def wrapper(*args, **kwargs):
        if len(args) == 1:
            key = (func.__name__, [v for v in args][0])
        else:
            key = (func.__name__, [v for k, v in kwargs.items()][0])
        if m.has_call(key) is None:
            val = func(*args, **kwargs)
            m.add_call(key, val)
            return val
        else:
            return f"value already calculated:{m.has_call(key)}"

    return wrapper


@lastcall
def param_function(num: int):
    return num * 2


param_function(3)
print()
param_function(num=3)
