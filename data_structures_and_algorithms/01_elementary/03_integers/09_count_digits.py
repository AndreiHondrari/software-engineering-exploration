

def count_digits(n: int) -> int:
    # count digits
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    numbers = [
        0, 1, 5, 10, 15, 111, 555_555_555
    ]

    for n in numbers:
        result: int = count_digits(n)
        print(f"{n} -> #{result} digits")
