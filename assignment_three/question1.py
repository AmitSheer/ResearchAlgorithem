from numbers import Number


class bounded_subsets:
    def __init__(self, s: list[Number], sum: Number):
        self.sum = sum
        self.array = s
        self.max_subset = pow(2, len(s))
        self.current_subset = 1
        self.stop = False
        self.max_elements = 0
        total = 0
        for i in s:
            total += i
            if total <= self.sum:
                self.max_elements += 1
            else:
                break

    def __iter__(self):
        return self

    def __next__(self):
        # using the Power Set Method to find the next subset that creates the sum
        # Set  = [a,b,c]
        # power_set_size = pow(2, 3) = 8
        # Run for binary counter = 000 to 111
        # Value of Counter            Subset
        #    000                    -> Empty set
        #    001                    -> a
        #    010                    -> b
        #    011                    -> ab
        #    100                    -> c
        #    101                    -> ac
        #    110                    -> bc
        #    111                    -> abc

        def get_array(el) -> (Number, list[Number]):
            if el.current_subset >= el.max_subset:
                raise StopIteration
            index = len(el.array) - 1
            index_values = [0] * len(el.array)
            temp_sum = el.current_subset
            array_len = 0

            while temp_sum > 0:
                index_values[index] = temp_sum % 2
                array_len += temp_sum % 2
                temp_sum = temp_sum // 2
                index -= 1
                if array_len > el.max_elements:
                    raise StopIteration
            el.current_subset += 1
            return sum(map(lambda x, y: x * y, index_values, el.array)), index_values

        if self.current_subset >= self.max_subset or self.stop:
            raise StopIteration
        self.stop = True
        total, index_values = get_array(self)
        while total > self.sum:
            total, index_values = get_array(self)

        self.stop = False
        array = []
        for i in range(len(self.array)):
            if index_values[i] == 1:
                array.append(self.array[i])
        return array
