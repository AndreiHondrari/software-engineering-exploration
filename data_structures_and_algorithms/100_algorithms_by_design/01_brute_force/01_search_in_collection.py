"""
Given a set of numbers find x
"""

import random
import functools

from typing import List

hprint = functools.partial(print, "\n#")


def brute_search(
    items: List[int],
    reference: int,
) -> int:

    for i in range(len(items)):
        if items[i] == reference:
            return i

    return None


def main() -> None:
    values = [random.randint(0, 100) for _ in range(50)]
    hprint("Values")
    print(values)

    value_to_search = random.randint(0, 100)
    hprint("Searching:", value_to_search)

    result_index = brute_search(values, value_to_search)
    hprint("Result:", result_index)


if __name__ == "__main__":
    main()
