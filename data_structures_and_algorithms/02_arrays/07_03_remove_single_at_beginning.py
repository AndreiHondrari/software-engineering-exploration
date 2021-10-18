from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66]

    # Remove first one
    l2: List[int] = l1[1:]

    print(f"L1 {l1}")
    print(f"L2 {l2}")
