from unittest import TestCase

from assignment_4.part2.Graphs import GraphPath
from assignment_4.part2.question2 import shortest_path, greedy, brute_force
from question1 import bounded_subsets
from contextlib import redirect_stdout


class Test_shortest_path(TestCase):

    # check with and without name and greedy
    def test_shortest_path_greedy(self):
        self.assertEqual(6, shortest_path(greedy, [[0, 2, 3],
                                                   [2, 0, 1],
                                                   [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'],
                                          starting_city='TEL AVIV'))
        self.assertEqual(6, shortest_path(greedy, [[0, 2, 3],
                                                   [2, 0, 1],
                                                   [3, 1, 0]], starting_city='1'))
        self.assertEqual("TEL AVIV->NEW YORK->LA->TEL AVIV", shortest_path(greedy, [[0, 2, 3],
                                                                                    [2, 0, 1],
                                                                                    [3, 1, 0]],
                                                                           ['LA', 'TEL AVIV', 'NEW YORK'],
                                                                           starting_city='TEL AVIV',
                                                                           output_type=GraphPath))
        self.assertEqual("1->2->0->1", shortest_path(greedy, [[0, 2, 3],
                                                              [2, 0, 1],
                                                              [3, 1, 0]], starting_city='1', output_type=GraphPath))

    # check with and without name and brute_force
    def test_shortest_path_brute_force(self):
        self.assertEqual(6, shortest_path(brute_force, [[0, 2, 3],
                                                        [2, 0, 1],
                                                        [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'],
                                          starting_city='TEL AVIV'))
        self.assertEqual(6, shortest_path(brute_force, [[0, 2, 3],
                                                        [2, 0, 1],
                                                        [3, 1, 0]], starting_city='1'))
        self.assertEqual("TEL AVIV->LA->NEW YORK->TEL AVIV", shortest_path(brute_force, [[0, 2, 3],
                                                                                         [2, 0, 1],
                                                                                         [3, 1, 0]],
                                                                           ['LA', 'TEL AVIV', 'NEW YORK'],
                                                                           starting_city='TEL AVIV',
                                                                           output_type=GraphPath))
        self.assertEqual("1->0->2->1", shortest_path(brute_force, [[0, 2, 3],
                                                                   [2, 0, 1],
                                                                   [3, 1, 0]], starting_city='1',
                                                     output_type=GraphPath))

    # check with mixed lengths
    def test_shortest_path_different_distances(self):
        self.assertEqual(6, shortest_path(brute_force, [[0, 5, 3],
                                                        [2, 0, 1],
                                                        [7, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'],
                                          starting_city='TEL AVIV'))
        self.assertEqual(6, shortest_path(brute_force, [[0, 5, 3],
                                                        [2, 0, 1],
                                                        [7, 1, 0]], starting_city='1'))
        self.assertEqual("TEL AVIV->LA->NEW YORK->TEL AVIV", shortest_path(brute_force, [[0, 5, 3],
                                                                                         [2, 0, 1],
                                                                                         [3, 1, 0]],
                                                                           ['LA', 'TEL AVIV', 'NEW YORK'],
                                                                           starting_city='TEL AVIV',
                                                                           output_type=GraphPath))
        self.assertEqual("1->0->2->1", shortest_path(brute_force, [[0, 5, 3],
                                                                   [2, 0, 1],
                                                                   [7, 1, 0]], starting_city='1',
                                                     output_type=GraphPath))
        self.assertEqual(13, shortest_path(greedy, [[0, 5, 3],
                                                    [2, 0, 1],
                                                    [7, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'],
                                           starting_city='TEL AVIV'))
        self.assertEqual(13, shortest_path(greedy, [[0, 5, 3],
                                                    [2, 0, 1],
                                                    [7, 1, 0]], starting_city='1'))
        self.assertEqual("TEL AVIV->NEW YORK->LA->TEL AVIV", shortest_path(greedy, [[0, 5, 3],
                                                                                    [2, 0, 1],
                                                                                    [7, 1, 0]],
                                                                           ['LA', 'TEL AVIV', 'NEW YORK'],
                                                                           starting_city='TEL AVIV',
                                                                           output_type=GraphPath))
        self.assertEqual("1->2->0->1", shortest_path(greedy, [[0, 5, 3],
                                                              [2, 0, 1],
                                                              [7, 1, 0]], starting_city='1', output_type=GraphPath))
