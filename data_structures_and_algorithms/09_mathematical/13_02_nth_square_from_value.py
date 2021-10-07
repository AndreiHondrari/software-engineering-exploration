"""
Formula determine by analysing the properties of the offset
between starting from 1 and starting from an arbitrary value.

s=0 -> n**2     = n**2 + 2 * 0 * n + 0**2
s=1 -> (n+1)**2 = n**2 + 2 * 1 * n + 1**2
s=2 -> (n+2)**2 = n**2 + 2 * 2 * n + 2**2
s=k -> (n+k)**2 = n**2 + 2 * k * n + k**2

now if we reinterpret the starting point (s) as being a square of a value (sq),
then our new formula is:
f(n, sq) = n**2 + 2 * sqrt(sq) * n + sq

The condition that is introduced is that we must always provide the function
with a perfect square value.
"""
import math


def nth_square_from(
    n: int,
    start: int = 0
) -> int:
    assert start == 0 or start != 0 and start % math.sqrt(start) == 0, \
        "starting value must be a perfect square"

    return int(n**2 + 2 * math.sqrt(start) * n + start)


if __name__ == '__main__':
    for x in range(10+1):
        val = nth_square_from(x, 9)
        print(f"{x} -> {val}")
