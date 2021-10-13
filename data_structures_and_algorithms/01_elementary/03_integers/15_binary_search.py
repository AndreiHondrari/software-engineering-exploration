"""
Useful only if we have a extremely large number that has
multiple digits repeated, but that is rarely the case and
a simple linear search would suffice.
"""

from typing import Tuple, Optional


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def search_binary(n: int, ref: int) -> Tuple[bool, Optional[int]]:
    no_of_digits: int = count_digits(n)
    found: bool = False

    if no_of_digits == 1:
        if n == ref:
            found = True
    else:
        low: int = 0
        high: int = no_of_digits
        diff = high - low

        while diff >= 2:
            diff = high - low
            mid: int = diff // 2 + low

            # extract mid digit
            mid_digit: int = int(n // 10**mid % 10)

            print(low, mid, high, mid_digit)
            # perform comparisons
            if ref == mid_digit:
                found = True
                break

            if ref < mid_digit:
                low = mid
            elif ref > mid_digit:
                high = mid

    return found, mid if found else None


if __name__ == '__main__':
    a: int = 111233444578888888889999999999999
    reference: int = 1

    print(f"Search {reference} in {a}")

    found, pos = search_binary(a, reference)

    if found:
        print(f"Found at {pos}")
    else:
        print("Not found")
