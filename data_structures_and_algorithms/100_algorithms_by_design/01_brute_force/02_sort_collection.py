"""

"""
import random
import functools
import copy

from typing import List, Tuple

hprint = functools.partial(print, "\n#")


def brute_sort(unsorted_items: List[int]) -> Tuple[int, ...]:
    """
    Bubble sort
    """

    sorted_values = copy.copy(unsorted_items)

    is_changed = True
    while is_changed:
        is_changed = False

        for i in range(len(sorted_values) - 1):
            a = sorted_values[i]
            b = sorted_values[i + 1]

            if a > b:
                sorted_values[i] = b
                sorted_values[i + 1] = a
                is_changed = True

    return tuple(sorted_values)


def main() -> None:
    values = [random.randint(1, 100) for _ in range(random.randint(30, 50))]

    hprint("Unsorted values")
    print(values)

    hprint("Sorted values")
    sorted_values = brute_sort(values)
    print(sorted_values)


if __name__ == "__main__":
    main()
