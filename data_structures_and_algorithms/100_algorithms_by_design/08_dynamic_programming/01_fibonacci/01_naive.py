

def fib(n: int) -> int:
    """
    Exponential time complexity
    due to extra call for each value

    O(2^n)
    """
    assert n > 0

    if n == 1 or n == 2:
        return 1

    return fib(n-2) + fib(n-1)


def main() -> None:
    values = list(range(1, 32 + 1))

    for x in values:
        y = fib(x)
        print(x, "->", y)


if __name__ == "__main__":
    main()
