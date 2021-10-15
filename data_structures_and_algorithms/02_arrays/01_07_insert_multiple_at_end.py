from typing import List


if __name__ == '__main__':
    l1: List[int] = [1, 2, 3, 4, 5]
    new_items: List[int] = [66, 77, 88, 99]

    l2: List[int] = l1 + new_items
    print("BEFORE: ", l1)
    print("AFTER:  ", l2)
