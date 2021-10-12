

if __name__ == '__main__':
    x = 123456789

    # count digits
    total_digit_count: int = 0
    n_copy: int = x
    while n_copy > 0:
        total_digit_count += 1
        n_copy = n_copy // 10

    for i in range(9):
        y = (x // 10**(total_digit_count - i - 1)) % 10
        print(y)
