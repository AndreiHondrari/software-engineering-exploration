from typing import List


if __name__ == '__main__':
    array1: List[int] = [
        66, 33, 88, 55, 77, 22, 99, 77, 11, 100, 200,
        300, 77, 77, 400, 500, 600, 77
    ]
    REFERENCE: int = 77

    print(f"array: {array1}")
    print(f"ref: {REFERENCE}")

    discovered_indexes: List[int] = []

    for i in range(len(array1)):
        if array1[i] == REFERENCE:
            discovered_indexes.append(i)

    print(f"Found at {discovered_indexes}")
