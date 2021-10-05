"""
Gcd of multiple numbers is achieved by composing the gcd calls.
The result of the gcd of numbers 'a' and 'b' can be used as
a parameter for the gcd with 'c'.
The resulting gcd will be the gcd of a, b, and c.
"""
from time import time


def gcd(a: int, b: int) -> int:
    assert a > 0 and b > 0, "Values must be greater than 0"
    m = min(a, b)
    n = max(a, b)

    q = n // m
    r = n - m * q
    last_r = m
    while r > 0:
        q = n // m
        last_r = r
        r = n - m * q
        n = m
        m = r

    return last_r


if __name__ == '__main__':
    a = 3**2 * 7**2
    b = 2**2 * 3**4 * 5**2
    c = 3**3

    result = gcd(a, b)
    result = gcd(result, c)
    print(f"gcd({a}, {b}, {c}) = {result}")
