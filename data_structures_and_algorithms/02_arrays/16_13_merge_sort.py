from typing import List


def merge(
    array: List[int],
    start_index: int,
    middle_index: int,
    end_index: int,
) -> List[int]:
    pass


def mergesort(
    array: List[int],
    start_index: int,
    end_index: int
) -> None:

    if (end_index - start_index) <= 1:
        return

    middle_index: int = (start_index + end_index) // 2
    print("MX", middle_index)

    mergesort(array, start_index, middle_index)
    mergesort(array, middle_index + 1, end_index)
    merge(array, start_index, middle_index, end_index)


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]

    print(f"BEFORE: {array}")

    mergesort(array, 0, len(array) - 1)

    print(f"AFTER:  {array}")
