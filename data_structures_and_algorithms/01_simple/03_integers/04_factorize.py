from typing import List


def factorize(n: int) -> List[int]:
    """
    Divid a number continuously by each value from 2 to n,
    until the result is 1 (meaning the last factor was used for division).
    Division has to happen only if there are no remainders.
    If there are remainders, then the factor candidate is actually
    not a factor of our number.

    Example:
    300 = 2 * 2 * 3 * 5 * 5

    300 / 2 = 150 remainder 0
    150 / 2 = 75 remainder 0
    75 / 2 = 37 remainder 1 -> ignore
    75 / 3 = 25 remainder 0
    25 / 3 = 8 remainder 1 -> ignore
    25 / 4 = 6 remainder 1 -> ignore
    25 / 5 = 5 remainder 0
    5 / 5 = 1 -> done
    """

    factors = []
    k = 2
    while n > 1:
        if n % k == 0:
            while n > 1:
                if n % k != 0:
                    break
                n = n // k
                factors.append(k)
        k += 1
    return factors


if __name__ == '__main__':
    numbers = [
        2**5 * 3**3 * 5**3 * 7**2 * 11**9 * 53155123,
        130,
        720,
        730,
        840,
    ]

    for n in numbers:
        results = factorize(n)
        print(f"Factorize {n}")
        print(results, end="\n\n")
