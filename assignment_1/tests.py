import math
import unittest
from question3 import find_root
from question1 import safe_call
from question2 import print_sorted


def func(name: str, id: int, age: float):
    return f"{name}, {id}, {age}"


def calc(x1: int, x2: float, x3: float):
    return x1 + x2 + x3


class MyTestCase(unittest.TestCase):
    def test_function_for_square_root_of_2(self):
        ff = lambda x: x ** 2 - 4
        self.assertEqual(round(find_root(ff, 2, 3)), 2)  # add assertion here

    def test_safe_call(self):
        self.assertEqual(6, safe_call(calc, 1, 2., 3.))
        with self.assertRaises(TypeError):
            safe_call(calc, 1, "", 3)
        with self.assertRaises(Exception):
            safe_call(calc, 1, 3)

        self.assertEqual("asdad, 2, 3.0", safe_call(func, "asdad", 2, 3.))
        with self.assertRaises(Exception):
            safe_call(func, 1, 3)
        with self.assertRaises(TypeError):
            safe_call(func, 1, 1, 3)

    def test_print_sorted(self):
        print("cant check the out put")


if __name__ == '__main__':
    unittest.main()
