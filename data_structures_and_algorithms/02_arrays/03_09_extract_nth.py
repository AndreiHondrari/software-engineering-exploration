from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130]
    n_offset: int = 3

    l2: List[int] = l1[n_offset-1::n_offset]

    print("BEFORE: ", l1)
    print("AFTER: ", l2)
