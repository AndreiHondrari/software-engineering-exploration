from typing import List, Callable


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_multiple_of(factor: int) -> Callable[[int], bool]:
    return lambda x: x % factor == 0


def count_if(
    n_list: List[int],
    criteria_func: Callable[[int], bool]
) -> int:
    amount: int = 0

    for n in n_list:
        if criteria_func(n):
            amount += 1

    return amount


if __name__ == '__main__':
    l1: List[int] = [k for k in range(1, 30+1)]
    print(f"ORIGINAL: {l1}")

    res: int = 0

    res = count_if(l1, is_even)
    print(f"COUNT (EVEN): {res}")

    factor: int = 0

    factor = 3
    res = count_if(l1, is_multiple_of(factor))
    print(f"COUNT ({factor}s multiple): {res}")

    factor = 5
    res = count_if(l1, is_multiple_of(factor))
    print(f"COUNT ({factor}s multiple): {res}")

    factor = 7
    res = count_if(l1, is_multiple_of(factor))
    print(f"COUNT ({factor}s multiple): {res}")

    factor = 9
    res = count_if(l1, is_multiple_of(factor))
    print(f"COUNT ({factor}s multiple): {res}")

    factor = 21
    res = count_if(l1, is_multiple_of(factor))
    print(f"COUNT ({factor}s multiple): {res}")
