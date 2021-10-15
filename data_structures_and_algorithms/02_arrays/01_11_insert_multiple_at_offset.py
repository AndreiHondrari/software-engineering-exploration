from typing import List


if __name__ == '__main__':
    l1: List[int] = [1, 2, 3, 4, 5]
    new_items: List[int] = [66, 77, 88, 99]
    offset = 2

    l2: List[int] = l1[:offset] + new_items + l1[offset:]
    print("OFFSET: ", offset)
    print("BEFORE: ", l1)
    print("AFTER:  ", l2)
