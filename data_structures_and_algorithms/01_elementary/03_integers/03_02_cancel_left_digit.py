

if __name__ == '__main__':

    a: int = 12345
    DIGITS_COUNT: int = 5

    power_of_ten: int = (DIGITS_COUNT - 1)
    divider: int = 10**power_of_ten
    x = a % divider

    print(f"{a} % {divider} [10**{power_of_ten}] -> {x}")
