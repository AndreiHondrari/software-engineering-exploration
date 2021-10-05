"""
We can obtain the polynomial form by applying the differences table method.

n           0   1   2   3   4   5   ...
Σ(n**2)     0   1   5   14  30  55  ...
Δ1              1   4   9   16  25  ...
Δ2                  3   5   7   9   ...
Δ3                      2   2   2   ...

based on the table we now know that our formula is of the form:
f(n) = a * n**3 + b * n**2 + c * n + d

let's find out the coeficients:
n = 0 -> d = 0
n = 1 -> a + b + c + d = 1
n = 2 -> 8*a + 4*b + 2*c + d = 5
n = 3 -> 27*a + 9*b + 3*c + d = 14

we substitute d and obtain system of 3 equations with 3 variables:
a + b + c = 1
8*a + 4*b + 2*c = 5
27*a + 9*b + 3*c = 14

c = 1 - a - b
8*a + 4*b + 2 - 2*a - 2*b = 5
27*a + 9*b + 3 - 3*a - 3*b = 14

+ |  6*a + 2*b = 3  | * (-3)
  | 24*a + 6*b = 11 |
  -------------------
     6*a       = 2

-> a = 2/6 = 1/3
-> b = (3 - 6*a) / 2 = (3 - 2) / 2 = 1/2
-> c = 1 - 1/3 - 1/2 = (6 - 2 - 3)/6 = 1/6

hence, our formula is:
f(n) = (1/3) * n**3 + (1/2) * n**2 + (1/6) * n
"""
from time import time
from decimal import Decimal as D


def sum_of_squares_until_limit(limit: int) -> int:
    """
    Very fast summation, since it uses a formula instead
    of a loop.
    """
    return int(
        (D(1)/D(3)) * limit ** 3 +
        (D(1)/D(2)) * limit ** 2 +
        (D(1)/D(6)) * limit
    )


if __name__ == '__main__':
    numbers = [
        5, 10, 1_000_000, 5_000_000,
    ]
    for n in numbers:
        a = time()
        result = sum_of_squares_until_limit(n)
        b = time()
        print(f"{n} => {result} [{b-a:.2f}]s")
