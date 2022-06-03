
from typing import Dict, Optional


def fib(
    n: int,
    lookup: Optional[Dict[int, int]] = None
) -> int:
    assert n > 0

    if lookup is None:
        lookup = {}

    if n == 1 or n == 2:
        return 1

    if n in lookup:
        return lookup[n]

    result = fib(n-2, lookup) + fib(n-1, lookup)
    lookup[n] = result
    return result


def main() -> None:
    values = list(range(1, 100 + 1))

    for x in values:
        y = fib(x)
        print(x, "->", y)


if __name__ == "__main__":
    main()
