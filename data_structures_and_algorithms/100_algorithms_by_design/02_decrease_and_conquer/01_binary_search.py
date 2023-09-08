"""
Given a set of sorted numbers find x
"""

import random
import functools

from typing import List, Optional

hprint = functools.partial(print, "\n#")


def binary_search(
    items: List[int],
    reference: int,
    low: int = 0,
    high: Optional[int] = None
) -> Optional[int]:

    if high is None:
        high = len(items) - 1

    mid = (high + low) // 2

    if high == low and items[mid] == reference:
        return mid

    elif reference <= items[mid]:
        return binary_search(items, reference, low, mid)

    elif reference > items[mid]:
        return binary_search(items, reference, mid + 1, high)

    return None


def main() -> None:
    values = [random.randint(0, 100) for _ in range(random.randint(30, 50))]
    values = sorted(values)
    hprint("Values")
    print(values)

    # value_to_search = random.randint(0, 100)
    value_to_search = random.sample(values, 1)[0]
    hprint("Searching:", value_to_search)

    result_index = binary_search(values, value_to_search)
    hprint("Result:", result_index)


if __name__ == "__main__":
    main()
