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


def lcm(a: int, b: int) -> int:
    assert a > 0 and b > 0, "Values must be greater than 0"

    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    pairs = [
        (1, 1),
        (2, 3),
        (5, 7),
        (4, 6),
        (17, 23),
        (23, 23),
        (7919, 7727),
        (21_632, 154_421),
        (81_632, 154_421),
        (181_632, 154_421),
        (281_632, 354_421),
        (281_632, 1_354_421),
        (1_281_632, 1_354_421),
        (2_281_632, 3_354_421),
        (522_281_632, 583_354_421),
        (999_999_999_901_522_281_632, 999_999_999_999_583_354_421),
    ]

    for p, q in pairs:
        a = time()
        result = lcm(p, q)
        b = time()
        print(f"lcm({p}, {q}) = {result} [{(b-a):.2f}s]")
