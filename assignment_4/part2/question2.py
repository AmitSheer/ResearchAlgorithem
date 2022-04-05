import itertools
import random
import sys
from typing import Callable

from assignment_4.part2.Graphs import GraphLength, Graph, GraphPath


def shortest_path(algorithm: Callable, dist: list[list[float]], names: list[str] = None, starting_city: str = None,
                  output_type=GraphLength):
    # if no city names were given
    if names is None:
        names = [str(x) for x in range(0, len(dist))]

    # get the index of the start city if none was given
    if starting_city is None:
        starting_city = names.index(names[random.randint(0, len(names) - 1)])
    elif isinstance(starting_city, str):
        starting_city = names.index(starting_city)

    # run the algorithm
    graph = output_type(dist, names, starting_city)
    return algorithm(graph, starting_city)


# checks every possible path in the graph from starting point
def brute_force(graph: Graph, starting_city: int):
    min_dist = sys.maxsize
    paths = [x for x in range(0, len(graph.cities))]
    graph.visit(starting_city)
    paths.remove(starting_city)
    # goes over every possible permutations of the paths without starting point
    for path in itertools.permutations(paths, len(paths)):
        # first step in the path
        distance = graph.dist[starting_city][path[0]]
        curr = path[0]
        # calculates the distance of current path
        for i in path[0:]:
            distance += graph.dist[curr][i]
            curr = i
        # adds travel from last in path to starting point
        distance += graph.dist[curr][starting_city]
        if distance < min_dist:
            min_dist = distance
            best = path
    # runs the visit function for each graph type
    for c in best:
        graph.visit(c)
    return graph.output()


# follows the least "resistance" path for current city
def greedy(graph: Graph, starting_city: int):
    graph.visit(starting_city)
    curr = starting_city
    while graph.visited.__contains__(False):
        curr_dist = sys.maxsize
        next_city = 0
        for i in range(0, len(graph.cities)):
            # checks if already visited and if the current lowest distance is lower then other unvisited nodes
            if graph.visited[i] is False and curr_dist > graph.dist[curr][i]:
                curr_dist = graph.dist[curr][i]
                next_city = i
        graph.visit(next_city)
        curr = next_city
    return graph.output()


if __name__ == '__main__':
    print(shortest_path(greedy, [[0, 2, 3],
                                 [2, 0, 1],
                                 [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'], starting_city='TEL AVIV'))
    print(shortest_path(greedy, [[0, 2, 3],
                                 [2, 0, 1],
                                 [3, 1, 0]], starting_city='1'))
    print(shortest_path(greedy, [[0, 2, 3],
                                 [2, 0, 1],
                                 [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'], starting_city='TEL AVIV',
                        output_type=GraphPath))
    print(shortest_path(greedy, [[0, 2, 3],
                                 [2, 0, 1],
                                 [3, 1, 0]], starting_city='1', output_type=GraphPath))

    print(shortest_path(brute_force, [[0, 2, 3],
                                      [2, 0, 1],
                                      [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'], starting_city='TEL AVIV'))
    print(shortest_path(brute_force, [[0, 2, 3],
                                      [2, 0, 1],
                                      [3, 1, 0]], starting_city='1'))
    print(shortest_path(brute_force, [[0, 2, 3],
                                      [2, 0, 1],
                                      [3, 1, 0]], ['LA', 'TEL AVIV', 'NEW YORK'], starting_city='TEL AVIV',
                        output_type=GraphPath))
    print(shortest_path(brute_force, [[0, 2, 3],
                                      [2, 0, 1],
                                      [3, 1, 0]], starting_city='1', output_type=GraphPath))
