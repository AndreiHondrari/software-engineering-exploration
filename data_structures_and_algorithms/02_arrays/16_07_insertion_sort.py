from typing import List


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"BEFORE: {array}")

    key: int
    j: int

    for i in range(1, len(array)):
        key = array[i]  # keep copy of current value
        j = i - 1  # first item next to i on the left
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  # overwrite right with left at each j
            j = j - 1  # go left

        array[j + 1] = key  # overwrite the leftmost element that is LTE key

    print(f"AFTER:  {array}")
