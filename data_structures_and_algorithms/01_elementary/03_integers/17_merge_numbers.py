

def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    a: int = 1234
    b: int = 56789

    a_no_of_digits: int = count_digits(a)
    b_no_of_digits: int = count_digits(b)

    max_no_of_digits: int = max(a_no_of_digits, b_no_of_digits)
    new_length: int = a_no_of_digits + b_no_of_digits

    a_digit: int = 0
    b_digit: int = 0
    result: int = 0
    j: int = 0  # index in resulting number
    for i in range(max_no_of_digits):
        if i < a_no_of_digits:
            a_digit = int(a // 10**(a_no_of_digits - i - 1) % 10)
            result += a_digit * 10**(new_length - j - 1)
            j += 1

        if i < b_no_of_digits:
            b_digit = int(b // 10**(b_no_of_digits - i - 1) % 10)
            result += b_digit * 10**(new_length - j - 1)
            j += 1

    print(f"{a}, {b} -> \n{result}")
