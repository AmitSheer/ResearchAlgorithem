def print_list(ob: list):
    sorted_list = sorted(ob)
    for term in sorted_list:
        if type(term) == list:
            print(f"{term}:[", end="")
            print_list(term)
            print("]", end="")
        elif type(term) == dict:
            print(f"", end="{")
            print_dict(term)
            print("}", end="")
        elif type(term) == tuple:
            print("", end="(")
            print_tuple(term)
            print(")", end="")
        else:
            print(f"{term}", end="")
        if sorted_list.index(term) < len(sorted_list) - 1:
            print(f"", end=",")


def print_tuple(ob: tuple):
    sorted_list = sorted(ob)
    for term in sorted_list:
        if type(term) == list:
            print(f"{term}:[", end="")
            print_list(term)
            print("]", end="")
        elif type(term) == dict:
            print(f"", end="{")
            print_dict(term)
            print("}", end="")
        elif type(term) == tuple:
            print("", end="(")
            print_tuple(term)
            print(")", end="")
        else:
            print(f"{term}", end="")
        if sorted_list.index(term) < len(sorted_list) - 1:
            print(f"", end=",")


def print_dict(ob: dict):
    sorted_ob = sorted(ob.items())
    for term in sorted_ob:
        if type(term[1]) == list:
            print(f"{term[0]}:[", end="")
            print_list(term[1])
            print("]", end="")
        elif type(term[1]) == dict:
            print(f"{term[0]}", end="{")
            print_dict(term[1])
            print("}", end="")
        elif type(term[1]) == tuple:
            print(f"{term[0]}", end="(")
            print_tuple(term[1])
            print(")", end="")
        else:
            print(f"{term[0]}:{term[1]}", end="")
        if sorted_ob.index(term) < len(sorted_ob) - 1:
            print(f"", end=",")


def print_sorted(ob):
    if type(ob) == list:
        print(f"[", end="")
        print_list(ob)
        print("]", end="")
    elif type(ob) == dict:
        print(f"", end="{")
        print_dict(ob)
        print("}", end="")
    elif type(ob) == tuple:
        print(f"", end="(")
        print_tuple(ob)
        print(")", end="")


if __name__ == '__main__':
    x = {"a": [{"g": 1}], "c": 6, "b": [1, 3, 2, 4], "f": (1, 3, 2)}
    print_sorted(x)
