from typing import List, Callable


def is_less_than(
    value: int,
    reference: int
) -> bool:
    return value < reference


def is_multiplied_with(factor: int) -> Callable[[int, int], bool]:
    return lambda x, y: x * factor == y


def check_adjancents_if(
    n_list: List[int],
    check_func: Callable[[int, int], bool]
) -> bool:
    SIZE: int = len(n_list)

    i: int = 0
    j: int = i + 1

    while i < SIZE and j < SIZE:

        if not check_func(n_list[i], n_list[j]):
            return False

        i += 1
        j += 1

    return True


if __name__ == '__main__':
    l1: List[int] = [
        11, 33, 99, 297, 891, 2673, 8019, 24057, 72171, 216513
    ]
    print(f"ORIGINAL: {l1}")

    res: bool
    res = check_adjancents_if(l1, is_less_than)
    print(f"Is sorted: {res}")

    factor: int
    factor = 3
    res = check_adjancents_if(l1, is_multiplied_with(factor))
    print(f"Is multiplied with {factor}: {res}")

    factor = 5
    res = check_adjancents_if(l1, is_multiplied_with(factor))
    print(f"Is multiplied with {factor}: {res}")
