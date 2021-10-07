"""
By analysing the summation: 1 + 2 + 3 + ... + n
we can determine a formula via two ways:
- differences table
- adding reverses

---
Differences table:

n   0   1   2   3   4   5   ...
Σn  0   1   3   6   10  15  ...
Δ1      1   2   3   4   5   ...
Δ2          1   1   1   1   ...

we conclude that our function is of the polynomial form:
f(n) = a * n**2 + b * n + c

let's find out the coeficients:
n = 0 -> c = 0
n = 1 -> a + b + c = 1
n = 2 -> 4 * a + 2 * b + c = 3

we substitute c and obtain the system of two equations with two variables:
a + b = 1
4 * a + 2 * b = 3

b = 1 - a
4 * a + 2 - 2 * a = 3 -> 2 * a = 1 -> a = 1/2 -> b = 1 - 1/2 = 1/2

which means our formula is: f(n) = (1/2) * n**2 + (1/2) * n

---
Adding reverses
Sn = 1 + 2 +     3 +     ... + n
Sn = n + (n-1) + (n-2) + ... + 1
+
--------------------------------
2Sn = (1+n) + (2+n-1) + (3+n-2) + ... + (1+n)
2Sn = (1+n) + (1+n) + (1+n) ... n-times
2Sn = n * (1 + n)

which means our formula is:
Sn = (n * (1 + n)) / 2

if transformed to it's polynomial variant is:
Sn = (n + n**2) / 2 = (1/2) * n**2 + (1/2) * n

which is equivalent to the version from the differences table.
"""
from time import time


def sum_until_limit(limit: int) -> int:
    return int(
        0.5 * limit ** 2 + 0.5 * limit
    )


if __name__ == '__main__':
    numbers = [
        5, 10, 10_000_000, 50_000_000,
        100_000_000, 1_000_000_000,
    ]

    for n in numbers:
        a = time()
        result = sum_until_limit(n)
        b = time()
        print(f"{n} => {result} [{b-a:.2f}]s")
