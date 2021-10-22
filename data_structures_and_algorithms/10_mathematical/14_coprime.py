
def gcd(a: int, b: int) -> int:
    m = min(a, b)
    n = max(a, b)
    q = n // m
    r = n - m * q
    last_r = r
    while r > 0:
        q = n // m
        last_r = r
        r = n - m * q
        n = m
        m = r

    return last_r


if __name__ == '__main__':
    numbers = [
        (2**2 * 3**2, 2 * 5**3,),
        (14, 25,),
    ]

    for a, b in numbers:
        are_coprime = gcd(a, b) == 1
        print(f"{a}, {b}: {are_coprime}")
