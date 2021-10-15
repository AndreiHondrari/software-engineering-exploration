from typing import List


if __name__ == '__main__':
    l1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    NEW_ITEM: int = 777

    offset: int = 6

    l2: List[int] = l1[:offset] + [NEW_ITEM] + l1[offset:]

    print(f"Old {l1}")
    print(f"New {l2}")
