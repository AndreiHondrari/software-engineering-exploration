from typing import List


if __name__ == '__main__':
    array1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    left: List[int] = []
    right: List[int] = []

    LEFT_HALF_SIZE = len(array1) // 2
    RIGHT_HALF_SIZE = len(array1) - LEFT_HALF_SIZE

    for i in range(LEFT_HALF_SIZE):
        left.append(array1[i])

    for i in range(RIGHT_HALF_SIZE):
        right.append(array1[LEFT_HALF_SIZE + i])

    print(f"Left: {left}")
    print(f"Right: {right}")
