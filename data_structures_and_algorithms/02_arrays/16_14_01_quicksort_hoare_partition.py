from typing import List


def partition(
    array: List[int],
    low: int,
    high: int,
) -> int:
    mid: int = (low + high) // 2
    pivot: int = array[mid]

    i: int = low
    j: int = high

    while True:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # swap a[i] with a[j]
        temp: int = array[i]
        array[i] = array[j]
        array[j] = temp


def quicksort(
    array: List[int],
    low: int,
    high: int,
) -> None:

    # the if will break the recursivity
    if (low >= 0 and high >= 0 and low < high):
        p: int = partition(array, low, high)
        quicksort(array, low, p)  # includes p
        quicksort(array, p + 1, high)


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"BEFORE: {array}")

    quicksort(array, 0, len(array) - 1)
    print(f"AFTER:  {array}")
