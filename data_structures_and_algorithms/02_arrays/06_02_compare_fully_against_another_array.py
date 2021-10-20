from typing import List, Callable


def compare_by(
    array1: List[int],
    array2: List[int],
    compare_func: Callable[[int, int], bool],
    strict: bool = False
) -> bool:

    if strict:
        assert len(array1) == len(array2), (
            "Arrays must be equal in size"
        )

    SIZE: int = len(array1)

    for i in range(SIZE):
        if not compare_func(array1[i], array2[i]):
            return False

    return True


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66]
    l2: List[int] = [11, 22, 33, 44, 55, 66]
    l3: List[int] = [22, 44, 66, 88, 110, 132]

    print(f"L1: {l1}")
    print(f"L2: {l2}")
    print(f"L3: {l3}")

    res: bool

    res = compare_by(l1, l2, lambda a, b: a == b)
    print(f"l1 == l2: {res}")

    res = compare_by(l1, l3, lambda a, b: a == b)
    print(f"l1 == l3: {res}")

    res = compare_by(l1, l3, lambda a, b: a * 2 == b)
    print(f"l3 double of l1: {res}")
