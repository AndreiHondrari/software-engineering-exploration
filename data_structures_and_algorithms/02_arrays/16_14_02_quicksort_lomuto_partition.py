from typing import List


def partition(
    array: List[int],
    low: int,
    high: int,
) -> int:
    pivot: int = array[high]

    i: int = low - 1

    for j in range(low, high + 1):
        if array[j] <= pivot:
            i += 1

            # swap a[i] with a[j]
            temp: int = array[i]
            array[i] = array[j]
            array[j] = temp
    return i


def quicksort(
    array: List[int],
    low: int,
    high: int,
) -> None:

    # the if will break the recursivity
    if (low >= 0 and high >= 0 and low < high):
        p: int = partition(array, low, high)
        quicksort(array, low, p - 1)  # doesn't include p
        quicksort(array, p + 1, high)


if __name__ == '__main__':
    array: List[int] = [7, 2, 10, 1, 9, 6, 3, 4, 8, 5]
    print(f"BEFORE: {array}")

    quicksort(array, 0, len(array) - 1)
    print(f"AFTER:  {array}")
