from typing import List, Optional


def binary_search(
    array: List[int],
    reference: int,
    low: int = 0,
    high: Optional[int] = None
) -> Optional[int]:
    # nothing to find in empty arrays
    if len(array) == 0:
        return None

    if high is None:
        high = len(array) - 1

    mid: int = (low + high) // 2

    discovered_index: Optional[int] = None
    if array[mid] == reference:
        discovered_index = mid

    # search on left side if our ref is lesser than mid
    elif reference < array[mid]:
        discovered_index = binary_search(
            array, reference, low=low, high=mid-1
        )

    # search on right side if our ref is greater than mid
    else:
        discovered_index = binary_search(
            array, reference, low=mid+1, high=high
        )

    return discovered_index


if __name__ == '__main__':
    array1: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    REFERENCE: int = 77

    print(f"Array: {array1}")
    print(f"Reference: {REFERENCE}")

    discovered_index: Optional[int] = binary_search(array1, REFERENCE)
    is_found: bool = discovered_index is not None

    print(f"Is found: {is_found} at {discovered_index}")
