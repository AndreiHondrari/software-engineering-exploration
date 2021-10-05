

def reverse(n: int) -> int:
    """
    Reverse number by iteratively dividing with 10 until 0,
    extracting the right most digit each step of the process.
    """
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n = n // 10
    return reversed


def is_palindrome(n: int) -> bool:
    """
    A palindrome number equals its mirror.
    """
    return n == reverse(n)


if __name__ == '__main__':
    numbers = [
        1, 15, 22, 100, 101, 122, 232, 1000, 1001, 1111, 99799, 997799,
        1111122222333332222211111,
    ]

    for x in numbers:
        result = is_palindrome(x)
        print(f"{str(result): >5}: {x}")
