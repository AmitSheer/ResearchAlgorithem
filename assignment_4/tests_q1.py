import io
from unittest import TestCase
from question1 import bounded_subsets
from contextlib import redirect_stdout


class Test_bounded_subsets(TestCase):

    def test_correct_sublist(self):
        array = [1, 2, 3]
        array_iter = bounded_subsets(array, 3)
        self.assertEqual(array_iter.__next__(), [3])
        self.assertEqual(array_iter.__next__(), [2])
        self.assertEqual(array_iter.__next__(), [1])
        self.assertEqual(array_iter.__next__(), [1, 2])

    def test_right_order(self):
        f = io.StringIO()
        array = [1, 2, 3]
        with redirect_stdout(f):
            for subset in bounded_subsets(array, 4):
                print(subset)
            output = f.getvalue()
            self.assertEqual(output, "[3]\n[2]\n[1]\n[1, 3]\n[1, 2]\n")

    def test_with_big_numbers(self):
        f = io.StringIO()
        array = [1, 55, 20, 13, 11, 2, 3]
        with redirect_stdout(f):
            for subset in bounded_subsets(array, 11):
                print(subset)
            output = f.getvalue()
            self.assertEqual(output, "[11]\n[3]\n[2]\n[2, 3]\n[1]\n[1, 3]\n[1, 2]\n[1, 2, 3]\n")

    def test_throw_error(self):
        array = [10]
        with self.assertRaises(StopIteration):
            print(bounded_subsets(array, 5).__next__())
