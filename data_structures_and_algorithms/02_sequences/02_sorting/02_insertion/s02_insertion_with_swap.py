"""
Insertion sort
"""

from typing import List


if __name__ == '__main__':

    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"Input array:  {array}")

    # iterate over the elements of the array starting with the second
    for j in range(1, len(array)):
        # keep a reference of the value at j into a key variable.
        # the key is used for comparison and for insertion after any value
        # that is lower than the key
        key = array[j]

        # reference the position to the left of the key's position
        i = j - 1

        # go from the position of i to the left until
        # either the beginning of the array is reached or
        # a value that is lower than the key
        while i >= 0 and array[i] > key:

            # always override the value to the right of j, or otherwise said
            # always override a value with the one to its left
            temp_value = array[i + 1]
            array[i + 1] = array[i]
            array[i] = temp_value
            i = i - 1  # keep going left

    print(f"Sorted array: {array}")
