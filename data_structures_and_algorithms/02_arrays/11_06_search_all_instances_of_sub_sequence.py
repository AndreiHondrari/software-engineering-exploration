from typing import List


if __name__ == '__main__':

    array1: List[int] = [
        55, 66, 55, 66, 11, 22, 33, 22, 33, 77, 33, 22, 11, 33, 22,
        11, 22, 33, 88, 99, 11, 22, 55, 33, 11, 22, 33, 11, 22, 33,
    ]

    reference_array: List[int] = [11, 22, 33]

    assert len(reference_array) <= len(array1)

    found: bool
    discovery_indexes: List[int] = []
    # slide the reference onto the target array
    for i in range(len(array1) - len(reference_array) + 1):

        found = True

        # compare the arrays
        for j in range(len(reference_array)):
            if reference_array[j] != array1[i + j]:
                found = False
                break

        if found:
            discovery_indexes.append(i)

    print(f"Found at {discovery_indexes}")
