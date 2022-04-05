class List(list):
    def __init__(self, seq=()):
        super().__init__(seq)

    def __getitem__(self, *args):
        try:
            # args -> (indexes)
            current = super().__getitem__(args[0][0])
            for index in args[0][1:]:
                current = current[index]
        except:
            # args -> (index)
            current = super().__getitem__(args[0])
        return current

    def __setitem__(self, *args):
        try:
            # args -> ((indexes), value)
            current = super().__getitem__(args[0][0])
            for index in args[0][1:-1]:
                current = current[index]
            current[args[0][-1]] = args[1]
        except:
            # args -> (index, value)
            super().__setitem__(args[0], args[1])


if __name__ == "__main__":
    new_list = List([
        [[1, 2, 3], [3, 9, 1]],
        [[4, 5, 6], [6, 4, 5]]])
    k = List([1, 2, 3])
    print(k[1])

    new_list[0, 1] = 5
    new_list[0, 1] = 5
    print(new_list)
