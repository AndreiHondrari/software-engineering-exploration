from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66]
    l2: List[int] = [11, 22, 33, 777, 888, 999]

    print(f"L1: {l1}")
    print(f"L2: {l2}")

    res: bool
    index: int

    index = 2
    res = l1[index] == l2[index]
    print(f"\nl1[{index}] {l1[index]} == l2[{index}] {l2[index]}: {res}")

    index = 5
    res = l1[index] == l2[index]
    print(f"\nl1[{index}] {l1[index]} == l2[{index}] {l2[index]}: {res}")

    index = 5
    res = l1[index] < l2[index]
    print(f"\nl1[{index}] {l1[index]} < l2[{index}] {l2[index]}: {res}")
