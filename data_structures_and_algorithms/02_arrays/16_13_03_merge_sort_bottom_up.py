from typing import List


def merge(
    array: List[int],
    start_index: int,
    middle_index: int,
    end_index: int,
    target_array: List[int]
) -> None:

    i: int = start_index
    j: int = middle_index

    for k in range(start_index, end_index + 1):

        if i < middle_index and (j > end_index or array[i] <= array[j]):
            target_array[k] = array[i]
            i += 1
        else:
            target_array[k] = array[j]
            j += 1


def merge_sort(
    array: List[int],
    target_array: List[int]
) -> None:
    assert len(array) == len(target_array)

    SIZE: int = len(array)

    width: int = 1
    i: int
    while width < SIZE:

        i = 0
        while i < SIZE:
            merge(
                array,
                start_index=i,
                middle_index=min(i + width, SIZE - 1),
                end_index=min(i + 2*width, SIZE - 1),
                target_array=target_array
            )
            i += 2 * width

        array = target_array.copy()

        width = 2 * width


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"BEFORE: {array}")

    result_array: List[int] = array.copy()
    merge_sort(array, result_array)
    print(f"AFTER:  {result_array}")
