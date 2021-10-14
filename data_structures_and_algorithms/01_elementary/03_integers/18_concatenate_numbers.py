

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

    b_no_of_digits: int = count_digits(b)

    x: int = a * 10**b_no_of_digits + b

    print(f"{a}, {b} -> \n{x}")
