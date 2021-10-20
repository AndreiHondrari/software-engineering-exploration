from typing import List


def swap_in_array(array: List[int], a: int, b: int) -> None:
    array[a] = array[a] ^ array[b]
    array[b] = array[a] ^ array[b]
    array[a] = array[a] ^ array[b]


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"BEFORE: {array}")

    key: int
    j: int

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                swap_in_array(array, i, j)

    print(f"AFTER:  {array}")
