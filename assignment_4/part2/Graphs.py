from abc import abstractmethod


class Graph:
    def __init__(self, dist: list[list[float]], cities: list[str], start: str):
        self.cities = cities
        self.dist = dist
        self.curr = int(start)
        self.visited = [False] * len(cities)
        self.visited[self.curr] = True
        self.start = int(start)

    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def visit(self, c):
        self.visited[c] = True
        self.curr = c


# Graph for getting the visited path
class GraphPath(Graph):
    def __init__(self, dist: list[list[float]], cities: list[str], start: str = None):
        super().__init__(dist, cities, start)
        self.path = ""

    def output(self):
        return self.path + self.cities[self.start]

    def visit(self, c):
        self.path += self.cities[c] + "->"
        super().visit(c)


# graph for the length operations
class GraphLength(Graph):
    def __init__(self, dist: list[list[float]], cities: list[str], start: str = None):
        super().__init__(dist, cities, start)
        self.distance = 0

    def output(self):
        return self.distance + self.dist[self.curr][self.start]

    def visit(self, c):
        if c != self.curr:
            self.distance += self.dist[self.curr][c]
            super().visit(c)
