

def is_palindrome(n: int) -> bool:
    # count digits
    digit_count = 0
    n_copy = n
    while n_copy > 0:
        digit_count += 1
        n_copy //= 10

    # detect palindromeness
    while n > 1:
        p = 10 ** (digit_count - 1)
        np = n // p
        nq = n % 10

        if np != nq:
            return False

        n = (n - np * p) // 10
        digit_count -= 2

    return True


if __name__ == '__main__':
    numbers = [
        1, 15, 22, 100, 101, 122, 232, 1000, 1001, 1111, 99799, 997799,
        1111122222333332222211111,
    ]

    for x in numbers:
        result = is_palindrome(x)
        print(f"{str(result): >5}: {x}")
