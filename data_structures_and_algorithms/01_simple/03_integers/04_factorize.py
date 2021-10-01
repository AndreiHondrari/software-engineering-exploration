from typing import List


def factorize(n: int) -> List[int]:
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
    n = 2**5 * 3**3 * 5**3 * 7**2 * 11**9 * 53155123
    results = factorize(n)
    print(f"Factorize {n}")
    print(results)
