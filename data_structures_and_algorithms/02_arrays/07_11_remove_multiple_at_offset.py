from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    OFFSET: int = 4
    AMOUNT: int = 3

    # Remove at offset
    l2: List[int] = l1[:OFFSET] + l1[OFFSET+AMOUNT:]

    print(f"L1 {l1}")
    print(f"L2 {l2}")
