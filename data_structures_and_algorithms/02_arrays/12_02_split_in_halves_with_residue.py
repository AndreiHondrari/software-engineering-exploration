from typing import List


if __name__ == '__main__':
    array1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    left: List[int] = []
    right: List[int] = []
    residue: int

    HALF_SIZE = len(array1) // 2
    HAS_RESIDUE: bool = len(array1) % 2 != 0

    for i in range(HALF_SIZE * 2):
        if i < HALF_SIZE:
            left.append(array1[i])
        else:
            right.append(array1[i])

    if HAS_RESIDUE:
        residue = array1[-1:][0]

    print(f"Left: {left}")
    print(f"Right: {right}")
    print(f"Residue: {residue}")
