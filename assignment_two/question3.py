class List(list):
    def __init__(self, seq=()):
        super().__init__(seq)

    def __getitem__(self, *args):
        if len(args) > 1:
            current = super().__getitem__(args[0][0])
            for index in args[0][1:]:
                current = current[index]
        else:
            current = super().__getitem__(args[0])
        return current


new_list = list([
    [[1, 2, 3], [3, 9, 1]],
    [[4, 5, 6], [6, 4, 5]]])
k = List([1, 2, 3])
# a = new_list[0, 1, 1]
# a = new_list[0][1][1]
# print(a)
print(k[1])
