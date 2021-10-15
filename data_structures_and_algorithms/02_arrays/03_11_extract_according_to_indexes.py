from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130]
    indexes: List[int] = [0, 5, 6, 12]

    l2: List[int] = []
    for i in indexes:
        l2 = l2 + [l1[i]]

    print("BEFORE: ", l1)
    print("AFTER: ", l2)
