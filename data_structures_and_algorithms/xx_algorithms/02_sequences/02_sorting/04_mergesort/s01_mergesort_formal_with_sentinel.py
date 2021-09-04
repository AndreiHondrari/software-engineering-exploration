import math
from typing import List, Union, Optional


def merge(
    array: List[int],
    start_index: int,
    middle_index: int,
    end_index: int,
) -> None:
    # determine the left and right subarray sizes
    left_size = middle_index - start_index + 1  # array[first ... mid] size
    right_size = end_index - middle_index  # array[mid+1 ... end] size

    # create left and right work subarrays
    left_half: List[Optional[Union[int, float]]] = [
        None for _ in range(left_size + 1)  # +1 because we want a sentinel
    ]

    right_half: List[Optional[Union[int, float]]] = [
        None for _ in range(right_size + 1)  # +1 because we want a sentinel
    ]

    # setting sentinels
    left_sentinel_index = left_size
    left_half[left_sentinel_index] = math.inf  # infinity on last index

    right_sentinel_index = right_size
    right_half[right_sentinel_index] = math.inf  # infinity on last index

    # distribute elements between left and right work subarrays
    for i in range(left_size):
        left_half[i] = array[start_index + i]

    for j in range(right_size):
        right_half[j] = array[middle_index + 1 + j]

    # zip the left and right subarray elements together, in order
    i = 0
    j = 0
    for k in range(start_index, end_index + 1):  # for A[start ... end]
        if left_half[i] <= right_half[j]:  # type: ignore
            array[k] = left_half[i]  # type: ignore
            i += 1
        else:
            array[k] = right_half[j]  # type: ignore
            j += 1


def merge_sort(
    array: List[int],
    start_index: int,
    end_index: int
) -> None:

    if start_index >= end_index:
        return

    middle_index = (start_index + end_index) // 2

    merge_sort(array, start_index, middle_index)
    merge_sort(array, middle_index+1, end_index)

    merge(array, start_index, middle_index, end_index)


if __name__ == '__main__':

    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"Input array:  {array}")

    merge_sort(array, 0, len(array) - 1)

    print(f"Sorted array: {array}")
