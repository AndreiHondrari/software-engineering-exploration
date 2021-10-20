from typing import List


if __name__ == '__main__':
    array1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"BEFORE: {array1}")

    # map values
    for i in range(len(array1)):
        array1[i] = array1[i] * 10

    print(f"AFTER:  {array1}")
