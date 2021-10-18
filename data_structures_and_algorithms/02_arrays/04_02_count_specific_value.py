from typing import List


if __name__ == '__main__':
    l1: List[int] = [
        1, 2, 3, 4, 777, 5, 6, 777, 7, 8, 9, 777, 10, 777, 777, 11
    ]

    REFERENCE_VALUE: int = 777

    amount: int = 0

    for n in l1:
        if n == 777:
            amount += 1

    print(f"ORIGINAL: {l1}")
    print(f"REFERENCE: {REFERENCE_VALUE}")
    print(f"COUNT: {amount}")
