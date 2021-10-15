from typing import List


if __name__ == '__main__':
    l1: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # for even positions
    l2: List[int] = l1[0::2]

    # for odd positions
    l3: List[int] = l1[1::2]

    print("ORIGINAL: ", l1)
    print("EVEN POSITIONS: ", l2)
    print("ODD POSITIONS:  ", l3)
