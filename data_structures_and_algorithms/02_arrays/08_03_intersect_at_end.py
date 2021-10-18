from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55]
    l2: List[int] = [66, 77, 88, 99, 110]

    L1SIZE: int = len(l1)
    L2SIZE: int = len(l2)

    assert L1SIZE == L2SIZE, "Arrays must be equal"

    print(f"L1        {l1}")
    print(f"L2 BEFORE {l2}")

    l2[L1SIZE - 1] = l1[L1SIZE - 1]  # the actual overwrite

    print(f"L2 AFTER  {l2}")
