from typing import List


def merge_by_criteria(
    array1: List[int],
    array2: List[int],
) -> List[int]:
    A1SIZE: int = len(array1)
    A2SIZE: int = len(array2)

    array3: List[int] = []

    i: int = 0
    j: int = 0

    # distribute by comparison
    while i < A1SIZE and j < A2SIZE:
        if array1[i] <= array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1

    # distribute residue
    while i < A1SIZE:
        if i < A1SIZE:
            array3.append(array1[i])
            i += 1

    while j < A2SIZE:
        if j < A2SIZE:
            array3.append(array2[j])
            j += 1

    return array3


if __name__ == '__main__':
    # notice they are of equal size
    array1: List[int] = [11, 22, 33]
    array2: List[int] = [44, 55, 66, 77, 88, 99]

    print(f"A1: {array1}")
    print(f"A2: {array2}")

    array3: List[int] = merge_by_criteria(array1, array2)
    print(f"A3: {array3}")
