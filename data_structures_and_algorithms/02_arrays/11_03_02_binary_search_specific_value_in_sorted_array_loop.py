from typing import List, Optional


if __name__ == '__main__':
    array1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    REFERENCE: int = 77

    print(f"Array: {array1}")
    print(f"Reference: {REFERENCE}")

    # perform search

    discovered_index: Optional[int] = None
    low: int = 0
    high: int = len(array1) - 1
    mid: int

    while low <= high and discovered_index is None:
        mid = (low + high) // 2

        if array1[mid] == REFERENCE:
            discovered_index = mid
        elif REFERENCE < array1[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print(f"Found at {discovered_index}")
