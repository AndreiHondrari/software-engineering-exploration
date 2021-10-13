from typing import Tuple, Optional


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def search_linearly(n: int, ref: int) -> Tuple[bool, Optional[int]]:
    no_of_digits: int = count_digits(n)

    found: bool = False
    for i in range(no_of_digits):
        # extract digit
        digit = n // 10**i % 10

        # compare digit
        if digit == reference:
            found = True
            break

    return found, i if found else None


if __name__ == '__main__':
    a: int = 842917850290584215521
    reference: int = 7

    print(f"Search {reference} in {a}")

    found, pos = search_linearly(a, reference)

    if found:
        print(f"Found at {pos}")
    else:
        print("Not found")
