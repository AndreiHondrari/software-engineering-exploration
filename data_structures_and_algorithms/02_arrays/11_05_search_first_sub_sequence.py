from typing import List, Optional


if __name__ == '__main__':

    array1: List[int] = [55, 66, 55, 66, 11, 22, 33, 22, 33]

    reference_array: List[int] = [11, 22, 33]

    assert len(reference_array) <= len(array1)

    found: bool
    discovery_index: Optional[int] = None
    # slide the reference onto the target array
    for i in range(len(array1) - len(reference_array)):

        found = True

        # compare the arrays
        for j in range(len(reference_array)):
            if reference_array[j] != array1[i + j]:
                found = False
                break

        if found:
            discovery_index = i
            break

    print(f"Is found: {found} at {discovery_index}")
