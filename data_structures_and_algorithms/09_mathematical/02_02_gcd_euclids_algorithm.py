from time import time


def gcd(a: int, b: int) -> int:
    """
    Based on division with remainders.

    Example:
    18 = 3 * 3 * 2
    45 = 3 * 3 * 5

    Obviously by looking at the factors, the gcd is 3 * 3 = 9.
    To discover it algorithmically one must divide and use the remainder
    as next in line for division.

    We always start with the bigger number:
    45 / 18 = 2 remainder 9
    18 / 9 = 2 remainder 0

    Because the remainder is 0, we don't need to divide any longer.
    It also means that 45 = 18 * (2 + 1/2).

    The 1/2 is the remainder that we are interested in, which is the gcd
    of the two. 18 * 1/2 = 9 = 3 * 3 .
    """
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
    pairs = [
        (1, 1),
        (5, 6),
        (6, 12),
        (14, 25),
        (15, 25),
        (182, 221),  # 14*13, 17*13 => 13
        (910, 1105),  # 14*13*5, 17*13*5 => 13*5 = 65
        (2730, 3315),  # 14*13*15, 17*13*15 => 14*13*3*5, 17*13*3*5 => 195
        (35209, 1307939),
        (58735223, 25190339),
        (17**20, 23**20 * 17**19),
    ]

    for p, q in pairs:
        a = time()
        result = gcd(p, q)
        b = time()
        print(f"gcd({p}, {q}) = {result} [{(b-a):.2f}s]")
