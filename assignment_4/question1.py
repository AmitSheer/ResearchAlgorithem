from numbers import Number


class bounded_subsets:
    def __init__(self, s: list[Number], sum: Number):
        # L = list(filter(None, s))  # ignore zeroes
        # if any(a < 0 < b for a, b in zip(L, L[1:])):
        #     raise Exception('invalid array')
        self.sum = sum
        self.array = sorted(s)
        self.current_subset = 1
        # self.stop = False
        self.max_elements = 0
        for i in s:
            if i > sum:
                self.array.remove(i)
        self.max_subset = pow(2, len(self.array))

        total = 0
        for i in self.array:
            total += i
            if total <= self.sum:
                self.max_elements += 1
            else:
                break

    def __iter__(self):
        return self

    def __next__(self):

        self.stop = True
        while self.stop:
            self.stop = False
            if self.current_subset >= self.max_subset:
                raise StopIteration
            composition = "{0:b}".format(self.current_subset).zfill(len(self.array))
            self.current_subset += 1
            if sum(map(lambda x, y: int(x) * y, composition, self.array)) <= self.sum:
                array = []
                for i in range(0, len(self.array)):
                    if int(composition[i]) == 1:
                        array.append(self.array[i])
                return array
            else:
                self.stop = True
