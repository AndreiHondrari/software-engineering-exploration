from typing import List


if __name__ == '__main__':
    array1: List[int] = [
        11, 22, 33, 44, 55, 66, 77, 88, 99, 100,
    ]

    reference_pattern_indexes: List[int] = [
        False, True, True, False, False,
        True, False, True, True, True,
    ]

    assert len(array1) == len(reference_pattern_indexes), (
        "The array and pattern indexes list must have equal size"
    )

    SIZE: int = len(array1)

    direct: List[int] = []
    opposite: List[int] = []

    # distribute items
    for i in range(SIZE):
        # direct items
        if reference_pattern_indexes[i]:
            direct.append(array1[i])

        # opposite items
        else:
            opposite.append(array1[i])

    # display
    array1_repr: str = ", ".join([
        f"{e: >3}" for e in array1
    ])
    pattern_repr: str = ", ".join([
        f"{e: >3}" for e in reference_pattern_indexes
    ])
    print(f"array:    [{array1_repr}]")
    print(f"pattern:  [{pattern_repr}]")
    print(f"direct:   {direct}")
    print(f"opposite: {opposite}")
