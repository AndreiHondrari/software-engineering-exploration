from typing import List


if __name__ == '__main__':
    l1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    amount: int = 7
    offset: int = 4

    l2: List[int] = l1[offset:offset+amount]
    print("AMOUNT: ", amount)
    print("OFFSET: ", offset)
    print("BEFORE: ", l1)
    print("AFTER:  ", l2)
