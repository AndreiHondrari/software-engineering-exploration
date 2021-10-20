from typing import List, Callable


def map_array(
    array: List[int],
    alter_func: Callable[[int], int]
) -> List[int]:
    result_array: List[int] = []
    altered_value: int

    for i in range(len(array)):
        altered_value = alter_func(array[i])
        result_array.append(altered_value)

    return result_array


if __name__ == '__main__':
    array1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"A1: {array1}")

    array2: List[int] = map_array(array1, lambda x: x * 2)
    print(f"A2: {array2}")

    array3: List[int] = map_array(array1, lambda x: x ** 2)
    print(f"A3: {array3}")

    array4: List[int] = map_array(array1, lambda x: x * 10 + x)
    print(f"A4: {array4}")
