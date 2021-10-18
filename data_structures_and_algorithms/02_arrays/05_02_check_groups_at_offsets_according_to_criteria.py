from typing import List, Callable


def check_groups_by(
    n_list: List[int],
    group_offset_1: int,
    group_offset_2: int,
    group_length: int,
    check_func: Callable[[int, int], int]
) -> bool:
    NSIZE: int = len(n_list)

    assert group_offset_1 + group_length - 1 <= NSIZE, (
        "Group 1 size is overflowing that of the main array"
    )
    assert group_offset_2 + group_length - 1 <= NSIZE, (
        "Group 2 size is overflowing that of the main array"
    )

    for i in range(group_length):
        val1: int = n_list[group_offset_1 + i]
        val2: int = n_list[group_offset_2 + i]
        if not check_func(val1, val2):
            return False

    return True


if __name__ == '__main__':
    l1: List[int] = [
        1, 2, 3, 4, 55,  # 0 .. 4
        66, 77, 88, 9, 10,  # 5 .. 9
        11, 12, 777, 888, 999,  # 10 ... 14
        1000, 1, 2, 3, 4  # 15 ... 19
    ]
    print(f"ORIGINAL: {l1}")

    res: bool
    pos1: int
    pos2: int

    pos1 = 0
    pos2 = 16
    res = check_groups_by(l1, pos1, pos2, 4, lambda a, b: a == b)
    print(f"Equality (positions {pos1} and {pos2}): {res}")

    pos1 = 0
    pos2 = 17
    res = check_groups_by(l1, pos1, pos2, 4, lambda a, b: a == b)
    print(f"Equality (positions {pos1} and {pos2}): {res}")

    pos1 = 0
    pos2 = 8
    res = check_groups_by(l1, pos1, pos2, 4, lambda a, b: a + 8 == b)
    print(f"Offset with 8 (positions {pos1} and {pos2}): {res}")

    pos1 = 0
    pos2 = 10
    res = check_groups_by(l1, pos1, pos2, 4, lambda a, b: a + 8 == b)
    print(f"Offset with 8 (positions {pos1} and {pos2}): {res}")
