from time import time


def lcm(a: int, b: int) -> int:
    """
    Multiply each of the numbers one by one, alternatively based on the
    comparison between the two, until equilibrium is reached.
    The number found in the equilibrium is the least common multiple.
    """
    assert a > 0 and b > 0, "Values must be greater than 0"

    x = a
    y = b

    xindex = 1
    yindex = 1
    while True:
        if (x < y):
            xindex += 1
            x = a * xindex
        elif (x > y):
            yindex += 1
            y = b * yindex
        else:
            break

    return x


if __name__ == '__main__':
    pairs = [
        (1, 1),
        (2, 3),
        (5, 7),
        (4, 6),
        (12, 14),
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
    ]

    for p, q in pairs:
        a = time()
        result = lcm(p, q)
        b = time()
        print(f"lcm({p}, {q}) = {result} [{(b-a):.2f}s]")
