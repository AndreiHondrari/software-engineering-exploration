"""
Insertion sort
"""

from typing import List
from copy import copy


def reverse_insertion_sort_version_1(input_array: List[int]) -> List[int]:
    """
    Insertion sort

    Similar to normal ascending insertion sort but with only the
    comparison operator switched to look for bigger values insteaad of
    lower values.
    """
    array: List[int] = copy(input_array)

    for j in range(1, len(array)):
        key = array[j]

        i = j - 1

        # notice that we compare with < sign
        # (iterates until aa bigger value is found)
        while i >= 0 and array[i] < key:

            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key

    return array


def reverse_insertion_sort_version_2(input_array: List[int]) -> List[int]:
    """
    Insertion sort

    Algorithm rewritten to start from the end of the array and go in reverse
    towards the beginning of the array. It is basically opposite in
    functionality compared to the normal ascending insertion sort algorithm.
    """
    array: List[int] = copy(input_array)

    # starting from index 8 and value 8 and going to index 0
    # notice that len(array) = 10
    #   j = len(array) - 2 = 8
    #   therefor
    #   i = 9 (last index)
    for j in range(len(array) - 2, -1, -1):
        key = array[j]

        i = j + 1

        # cover items from i to 9 (which is < len(array), which is < 10)
        while i < len(array) and array[i] > key:
            array[i - 1] = array[i]
            i = i + 1

        array[i - 1] = key

    return array


if __name__ == '__main__':

    main_array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"Input array:  {main_array}")

    array1 = reverse_insertion_sort_version_1(main_array)
    print(f"v1 Sorted array: {array1}")

    array2 = reverse_insertion_sort_version_2(main_array)
    print(f"v2 Sorted array: {array2}")
