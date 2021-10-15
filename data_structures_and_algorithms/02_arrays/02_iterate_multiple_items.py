from typing import List

if __name__ == '__main__':
    l1: List[int] = [
        11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130
    ]

    for i in range(0, len(l1), 2):
        a: int = l1[i]

        b = None
        if i + 1 < len(l1):
            b: int = l1[i + 1]

        print(f"{a} {b}")
