from typing import List, Optional


def interpolation_search(array: List[int], reference: int) -> Optional[int]:
    if len(array) == 0:
        return None

    low: int = 0
    high: int = len(array) - 1

    while low < high and array[low] != array[high]:
        ref_low_val_diff: int = reference - array[low]
        high_low_val_diff: int = array[high] - array[low]
        ref_percentage: float = ref_low_val_diff / high_low_val_diff
        mid: int = int(low + (high - low) * ref_percentage)

        print(f"{mid}", end=" ")
        if array[mid] == reference:
            return mid

        if reference > array[mid]:
            low = mid + 1
        elif reference < array[mid]:
            high = mid - 1

    return None


if __name__ == '__main__':
    array1: List[int] = [
        1, 2, 5, 9, 11, 20, 21, 22, 40, 70, 90, 100, 110, 120,
        121, 122, 123, 124, 125, 126, 128, 129, 130, 140, 1000
    ]

    print(f"array1: {array1}\n")

    index: Optional[int]
    REF: int

    REF = 5
    index = interpolation_search(array1, REF)
    print(f"\nFOUND {REF} at {index}\n")

    REF = 128
    index = interpolation_search(array1, REF)
    print(f"\nFOUND {REF} at {index}\n")

    array2: List[int] = [i for i in range(10)]
    array2.append(10_000)

    print(f"array2: {array2}\n")

    REF = 9
    index = interpolation_search(array2, REF)
    print(f"\nFOUND {REF} at {index}\n")
