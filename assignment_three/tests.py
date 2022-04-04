from unittest import TestCase
from question1 import bounded_subsets


class Test_bounded_subsets(TestCase):

    def test_correct_sublist(self):
        array = [1, 2, 3]
        array_iter = bounded_subsets(array, 3)
        self.assertEqual(array_iter.__next__(), [3])
        self.assertEqual(array_iter.__next__(), [2])
        self.assertEqual(array_iter.__next__(), [1])
        self.assertEqual(array_iter.__next__(), [1, 2])

    def test_throw_error(self):
        array = [10]
        with self.assertRaises(StopIteration):
            bounded_subsets(array, 5).__next__()

