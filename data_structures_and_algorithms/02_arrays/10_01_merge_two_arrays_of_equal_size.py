from typing import List


if __name__ == '__main__':
    # notice they are of equal size
    array1: List[int] = [11, 22, 33, 44, 55]
    array2: List[int] = [66, 77, 88, 99, 110]

    assert len(array1) == len(array2), (
        "arrays must have equal size"
    )

    print(f"A1: {array1}")
    print(f"A2: {array2}")

    # initialize new array
    array3: List[int] = []

    for i in range(len(array1)):
        array3.append(array1[i])
        array3.append(array2[i])

    print(f"A3: {array3}")
