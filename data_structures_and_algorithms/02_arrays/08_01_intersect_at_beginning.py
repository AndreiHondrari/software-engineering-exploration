from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55]
    l2: List[int] = [66, 77, 88, 99, 110]

    print(f"L1        {l1}")
    print(f"L2 BEFORE {l2}")

    l2[0] = l1[0]  # the actual overwrite

    print(f"L2 AFTER  {l2}")
