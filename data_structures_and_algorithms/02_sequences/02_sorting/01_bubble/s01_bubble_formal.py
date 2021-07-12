"""
Bubble sort
"""

from typing import List
import time


if __name__ == '__main__':

    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"Input array:  {array}")

    # runs until there are no swaps happening
    while True:
        swapped = False  # reset the swap flag

        # goes over the entire array from second to pre-last
        # this for is done again and again until there is no swap
        for i in range(1, len(array)):

            # swaps every pair from left to right if
            # the left value is greater than the right value
            if array[i - 1] > array[i]:
                temporary_value = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temporary_value
                print(f"swap: {array} i={i}")
                swapped = True  # remember that there was a swap

        # after a full array sweep without a single swap we stop because
        # it means that the array is in order an no values needed
        # re-arranging, therefore it is pointless to continue comparing
        # pairs of values
        if not swapped:
            break

    print(f"Sorted array: {array}")
