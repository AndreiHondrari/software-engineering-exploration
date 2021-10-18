from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55]
    l2: List[int] = [66, 77, 88, 99, 110]
    OFFSET: int = 2

    L1SIZE: int = len(l1)
    L2SIZE: int = len(l2)

    assert L1SIZE == L2SIZE, "Arrays must be equal"

    print(f"L1 {l1}")
    print(f"L2 {l2}")

    l3: List[int] = [k for k in l1]

    l3[OFFSET] = l2[OFFSET]

    print(f"L3 {l3}")
