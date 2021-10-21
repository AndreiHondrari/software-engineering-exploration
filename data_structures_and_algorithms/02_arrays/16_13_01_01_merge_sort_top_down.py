from typing import List


def merge(
    array: List[int],
    start_index: int,
    middle_index: int,
    end_index: int,
    target_array: List[int]
) -> None:
    # start_index ... middle_index = left
    # middle_index+1 ... end_index = right

    i: int = start_index
    j: int = middle_index + 1
    k: int = start_index

    while i <= middle_index and j <= end_index:
        if array[i] <= array[j]:
            target_array[k] = array[i]
            i += 1
        else:
            target_array[k] = array[j]
            j += 1

        k += 1

    while i <= middle_index:
        target_array[k] = array[i]
        i += 1
        k += 1

    while j <= end_index:
        target_array[k] = array[j]
        j += 1
        k += 1


def split_merge(
    work_array: List[int],
    start_index: int,
    end_index: int,
    target_array: List[int]
) -> None:

    # when start_index is equal to end_index then it means there is
    # only one element in the range (inherently sorted)
    if (end_index - start_index) == 0:
        return

    middle_index: int = (start_index + end_index) // 2

    split_merge(target_array, start_index, middle_index, work_array)
    split_merge(target_array, middle_index + 1, end_index, work_array)
    merge(work_array, start_index, middle_index, end_index, target_array)


def merge_sort(array: List[int]) -> None:
    work_array: List[int] = array.copy()
    split_merge(work_array, 0, len(array) - 1, array)


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"BEFORE: {array}")

    merge_sort(array)

    print(f"AFTER:  {array}")
