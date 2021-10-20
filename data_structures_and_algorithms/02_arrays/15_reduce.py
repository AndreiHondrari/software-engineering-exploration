from typing import List, Callable, Optional, cast


def reduce_array(
    array: List[int],
    func: Callable[[int, int], int]
) -> Optional[int]:
    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0]

    result: Optional[int] = func(array[0], array[1])

    for i in range(2, len(array)):
        result = func(cast(int, result), array[i])

    return result


if __name__ == '__main__':
    result: Optional[int]

    # array 1
    array1: List[int] = [1, 10, 100, 1000, 10_000]
    print(f"A1: {array1}")

    result = reduce_array(array1, lambda x, y: x + y)
    print(f"R1: {result}")

    # array 2
    array2: List[int] = [2, 3, 5, 7]
    print(f"A2: {array2}")

    result = reduce_array(array2, lambda x, y: x * y)
    print(f"R2: {result}")
