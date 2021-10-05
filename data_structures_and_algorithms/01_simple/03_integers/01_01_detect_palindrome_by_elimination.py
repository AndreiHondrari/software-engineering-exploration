

def is_palindrome(n: int) -> bool:
    """
    Detect the palindrome property of an integer by comparing
    extreme digits of the number (most left and most right),
    eliminating each pair as the algorithm progresses.
    """
    # count digits
    digit_count = 0
    n_copy = n
    while n_copy > 0:
        digit_count += 1
        n_copy //= 10

    # detect palindromeness
    while n > 1:
        # extract the extreme digits
        p = 10 ** (digit_count - 1)  # 10 powered to the length of the number
        np = n // p  # get most left number by dividing with the 10 powered
        nq = n % 10  # get most right by dividing with 10 for the remainder

        # compare the extreme digits
        if np != nq:
            # if two digits don't match it doesn't make sense to continue
            return False

        # remove the extreme digits, reducing the form of the number
        n = (n - np * p) // 10
        digit_count -= 2  # make sure to keep account of the form reduction

    return True


if __name__ == '__main__':
    numbers = [
        1, 15, 22, 100, 101, 122, 232, 1000, 1001, 1111, 99799, 997799,
        1111122222333332222211111,
    ]

    for x in numbers:
        result = is_palindrome(x)
        print(f"{str(result): >5}: {x}")
