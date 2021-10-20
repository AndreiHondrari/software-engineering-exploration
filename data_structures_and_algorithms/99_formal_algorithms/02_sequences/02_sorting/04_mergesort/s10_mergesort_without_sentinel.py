"""
DEFECTED IMPLEMENTATION !!!!!

"""
from typing import List


def merge(
    array: List[int],
    start_index: int,
    middle_index: int,
    end_index: int,
) -> None:
    print(f"\n---- SI {start_index} MI {middle_index} EI {end_index} ---")
    # determine the left and right subarray sizes
    left_size = middle_index - start_index + 1  # array[first ... mid] size
    right_size = end_index - middle_index  # array[mid+1 ... end] size

    # create left and right work sub arrays
    left_half: List[int] = [
        0 for _ in range(left_size)
    ]

    right_half: List[int] = [
        0 for _ in range(right_size)
    ]

    # distribute elements between left and right work subarrays
    for i in range(left_size):
        left_half[i] = array[start_index + i]

    for j in range(right_size):
        right_half[j] = array[middle_index + 1 + j]

    print(f"L {left_half}")
    print(f"R {right_half}")

    # zip the left and right subarray elements together, in order
    i = 0
    j = 0
    for k in range(start_index, end_index + 1):  # for A[start ... end]

        print(f"\n---- K {k} -----")

        left_exists: bool = (i < left_size)
        right_exists: bool = (j < right_size)

        if (
            left_exists and (
                not right_exists or
                right_exists and left_half[i] <= right_half[j]
            )
        ):
            print("AAA")
            array[k] = left_half[i]
            i += 1
            print(f"#1 -> {array}")

        left_exists = (i < left_size)
        right_exists = (j < right_size)

        if (
            right_exists and (
                not left_exists or
                left_exists and left_half[i] > right_half[j]
            )
        ):
            print("BBB")
            array[k] = right_half[j]
            j += 1
            print(f"#2 -> {array}")


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
