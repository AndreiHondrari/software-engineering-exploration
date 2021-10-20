from typing import List


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"BEFORE: {array}")

    swap: bool
    j: int
    while True:
        swap = False
        for i in range(len(array) - 1):
            j = i + 1
            if array[i] > array[j]:
                array[i] = array[i] ^ array[j]
                array[j] = array[i] ^ array[j]
                array[i] = array[i] ^ array[j]
                swap = True

        if not swap:
            break

    print(f"AFTER:  {array}")
