from typing import List


if __name__ == '__main__':
    array1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    array2: List[int] = []

    print(f"A1: {array1}")

    # map values
    for i in range(len(array1)):
        array2.append(array1[i] * 10)

    print(f"A2: {array2}")
