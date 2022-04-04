import itertools
import sys
from numbers import Number
from typing import Callable


def shortest_path(algorithm: Callable, cities: list[str], dist: list[list[float]], starting_city: str):
    return algorithm(cities, dist, starting_city)


def greedy(cities: list[str], dist: list[list[float]], starting_city: str) -> (list[str], Number):
    min_dist = sys.maxsize
    min_path = []
    start_index = cities.index(starting_city)
    paths = [x for x in range(0, len(cities))]
    paths.remove(start_index)

    for path in itertools.permutations(paths, len(paths)):
        distance = dist[start_index][paths[0]]
        curr = paths[0]
        for i in path[0:]:
            distance += dist[curr][i]
            curr = i
        distance = dist[curr][start_index]
        if distance < min_dist:
            distance = shortest_path
            min_path = path
    min_path.append(start_index)
    min_path.insert(0, start_index)
    return [cities[i] for i in min_path], min_dist

