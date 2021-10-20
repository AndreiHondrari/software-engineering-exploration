from typing import List


if __name__ == '__main__':
    # notice they are of equal size
    array1: List[int] = [11, 22, 33]
    array2: List[int] = [44, 55, 66, 77, 88, 99]

    assert len(array1) != len(array2), (
        "arrays must have different sizes"
    )

    print(f"A1: {array1}")
    print(f"A2: {array2}")

    A1SIZE: int = len(array1)
    A2SIZE: int = len(array2)
    MAX_SIZE: int = max(A1SIZE, A2SIZE)

    array3: List[int] = []

    for i in range(MAX_SIZE):
        if i < A1SIZE:
            array3.append(array1[i])

        if i < A2SIZE:
            array3.append(array2[i])

    print(f"A3: {array3}")
