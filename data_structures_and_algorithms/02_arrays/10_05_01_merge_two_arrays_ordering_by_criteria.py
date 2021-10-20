from typing import List


def merge_by_criteria(
    array1: List[int],
    array2: List[int],
) -> List[int]:
    A1SIZE: int = len(array1)
    A2SIZE: int = len(array2)
    MAX_SIZE: int = max(A1SIZE, A2SIZE)
    MIN_SIZE: int = min(A1SIZE, A2SIZE)

    array3: List[int] = []
    first: int
    second: int

    for i in range(MAX_SIZE):
        # if only one array has elements
        # then take from that array
        if i >= MIN_SIZE:
            if i < A1SIZE:
                array3.append(array1[i])

            if i < A2SIZE:
                array3.append(array2[i])

        # if both arrays have elements, compare
        else:
            if array1[i] < array2[i]:
                first = array1[i]
                second = array2[i]
            else:
                first = array2[i]
                second = array1[i]

            array3.append(first)
            array3.append(second)

    return array3


if __name__ == '__main__':
    # notice they are of equal size
    array1: List[int] = [11, 22, 33]
    array2: List[int] = [44, 55, 66, 77, 88, 99]

    print(f"A1: {array1}")
    print(f"A2: {array2}")

    array3: List[int] = merge_by_criteria(array1, array2)
    print(f"A3: {array3}")
