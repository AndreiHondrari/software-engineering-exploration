from time import time


def gcd(a: int, b: int) -> int:
    min_val = min(a, b)

    for x in range(min_val, 0, -1):
        if a % x == 0 and b % x == 0:
            return x

    return 1


if __name__ == '__main__':
    pairs = [
        (5, 6),
        (6, 12),
        (15, 25),
        (182, 221),  # 14*13, 17*13 => 13
        (910, 1105),  # 14*13*5, 17*13*5 => 13*5 = 65
        (2730, 3315),  # 14*13*15, 17*13*15 => 14*13*3*5, 17*13*3*5 => 195
        (35209, 1307939),
        (58735223, 25190339),
    ]

    for p, q in pairs:
        a = time()
        result = gcd(p, q)
        b = time()
        print(f"gcd({p}, {q}) = {result} [{(b-a):.2f}s]")
