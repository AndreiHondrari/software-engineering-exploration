from typing import List, Callable


def merge_by_criteria(
    array1: List[int],
    array2: List[int],
    compare_func: Callable[[int, int], bool],
    selector_func: Callable[[int, int, bool], int]
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
            if compare_func(array1[i], array2[i]):
                first = selector_func(array1[i], array2[i], True)
                second = selector_func(array1[i], array2[i], False)
            else:
                first = selector_func(array1[i], array2[i], False)
                second = selector_func(array1[i], array2[i], True)

            array3.append(first)
            array3.append(second)

    return array3


def select_first() -> Callable[[int, int, bool], int]:
    return lambda first, second, cond: first if cond else second


def select_second() -> Callable[[int, int, bool], int]:
    return lambda first, second, cond: second if cond else first


if __name__ == '__main__':
    # notice they are of equal size
    array1: List[int] = [11, 22, 33]
    array2: List[int] = [44, 55, 66, 77, 88, 99]

    print(f"A1: {array1}")
    print(f"A2: {array2}")

    array3: List[int] = merge_by_criteria(
        array1, array2,
        compare_func=lambda x, y: x < y,
        selector_func=select_first()
    )
    print(f"A3: {array3}")

    array4: List[int] = merge_by_criteria(
        array1, array2,
        compare_func=lambda x, y: x < y,
        selector_func=select_second()
    )
    print(f"A4: {array4}")

    array5: List[int] = merge_by_criteria(
        array1, array2,
        compare_func=lambda x, y: x > y,
        selector_func=select_first()
    )
    print(f"A5: {array5}")

    array6: List[int] = merge_by_criteria(
        array1, array2,
        compare_func=lambda x, y: x > y,
        selector_func=select_second()
    )
    print(f"A6: {array6}")
