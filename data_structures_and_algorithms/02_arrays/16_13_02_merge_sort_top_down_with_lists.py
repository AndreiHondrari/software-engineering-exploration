from typing import List


def merge(
    array1: List[int],
    array2: List[int]
) -> List[int]:
    A1_SIZE: int = len(array1)
    A2_SIZE: int = len(array2)

    result_array: List[int] = []

    i: int = 0
    j: int = 0

    while i < A1_SIZE or j < A2_SIZE:
        if i < A1_SIZE and (j >= A2_SIZE or array1[i] < array2[j]):
            result_array.append(array1[i])
            i += 1
        else:
            result_array.append(array2[j])
            j += 1

    return result_array


def merge_sort(
    array: List[int]
) -> List[int]:

    if len(array) == 0:
        return []

    if len(array) == 1:
        return array

    middle_index: int = len(array) // 2

    left: List[int] = array[:middle_index]
    right: List[int] = array[middle_index:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"BEFORE: {array}")

    result_array: List[int] = merge_sort(array)
    print(f"AFTER:  {result_array}")
