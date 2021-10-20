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

    for i in range(1, len(array)):
        key = array[i]  # keep copy of current value
        j = i - 1  # first item next to i on the left
        while j >= 0 and array[j] > key:
            # swap every two adjancent items from i to 0
            swap_in_array(array, j+1, j)

            j = j - 1  # go left

    print(f"AFTER:  {array}")
