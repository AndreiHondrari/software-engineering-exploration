from typing import List, Optional


if __name__ == '__main__':
    array1: List[int] = [66, 33, 88, 55, 77, 22, 99, 11]
    REFERENCE: int = 77

    print(f"array: {array1}")
    print(f"ref: {REFERENCE}")

    discovered_index: Optional[int] = None
    is_found: bool = False
    for i in range(len(array1)):
        if array1[i] == REFERENCE:
            is_found = True
            discovered_index = i
            break

    print(f"Is found: {is_found} at {discovered_index}")
