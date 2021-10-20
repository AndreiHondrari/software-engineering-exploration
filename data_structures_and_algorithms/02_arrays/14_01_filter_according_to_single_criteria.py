from typing import List


if __name__ == '__main__':
    array1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    array2: List[int] = []

    # filter
    for k in array1:
        if k % 2 == 0:
            array2.append(k)

    print(f"A1 {array1}")
    print(f"A2 {array2}")
