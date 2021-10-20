from typing import List, Callable


if __name__ == '__main__':
    array1: List[int] = [
        11, 22, 33, 44, 55, 66, 77, 88, 99,
        110, 120, 130, 140, 150, 160, 170, 180, 190, 200
    ]
    array2: List[int] = []

    criteria_funcs: List[Callable[[int], bool]] = [
        lambda x: x % 2 == 0,
        lambda x: x > 50,
        lambda x: x % 3 == 0
    ]

    # filter
    for k in array1:
        if all([func(k) for func in criteria_funcs]):
            array2.append(k)

    print(f"A1 {array1}")
    print(f"A2 {array2}")
