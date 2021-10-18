from typing import List


if __name__ == '__main__':
    l1: List[int] = [
        1, 2, 3, 4, 7, 5, 6, 7, 7, 6, 6, 7, 10, 7, 7, 11,
        6, 8, 6, 2, 3, 5, 1, 2, 5, 7, 6, 7, 8, 2, 1,
    ]

    FIRST: int = 7
    SECOND: int = 6
    OFFSET: int = 2

    amount: int = 0

    i: int = 0
    j: int = i + OFFSET

    while i < len(l1) and j < len(l1):
        first: int = l1[i]
        second: int = l1[j]

        if first == FIRST and second == SECOND:
            amount += 1

        i += 1
        j = i + OFFSET

    print(f"ORIGINAL: {l1}")
    print(f"FIRST: {FIRST}")
    print(f"SECOND: {SECOND}")
    print(f"OFFSET: {OFFSET}")
    print(f"COUNT: {amount}")
