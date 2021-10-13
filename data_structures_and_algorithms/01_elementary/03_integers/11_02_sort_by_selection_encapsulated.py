"""
Perform selection sort by following the general algorithm:

iterate over complete collection:
    iterate over part of collection after current index of parent iterator
        compare elements of the two positions defined by the iterator indexes
            swap the values if they are not in order

The extraction of the digits as well as swapping are according
to the integer operations.

The operations are encapsulated in their own functions and through their
status as higher-order functions they are passed to the
selection sort function.
"""
from typing import Any, Callable
from copy import deepcopy


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def extract_from_number(number: int, position: int) -> int:
    return int(number // 10**position % 10)


def swap_digits(
    number: int,
    position_1: int,
    position_2: int
) -> int:
    digit_1: int = extract_from_number(number, position_1)
    digit_2: int = extract_from_number(number, position_2)

    old_1: int = digit_1 * 10**position_1
    old_2: int = digit_2 * 10**position_2

    new_1: int = digit_2 * 10**position_1
    new_2: int = digit_1 * 10**position_2

    return number - old_1 - old_2 + new_1 + new_2


def selection_sort(
    collection: Any,
    size: int,
    swap_func: Callable[[Any, int, int], Any],
    extract: Callable[[Any, int], Any],
) -> Any:
    sorted_collection = deepcopy(collection)

    for i in range(size):
        for j in range(i+1, size):
            element_1 = extract(sorted_collection, i)
            element_2 = extract(sorted_collection, j)

            if element_1 < element_2:
                sorted_collection = swap_func(sorted_collection, i, j)

    return sorted_collection


if __name__ == '__main__':
    a: int = 741672910385089
    no_of_digits: int = count_digits(a)

    x: int = selection_sort(a, no_of_digits, swap_digits, extract_from_number)

    print(f"{a} -> {x}")
