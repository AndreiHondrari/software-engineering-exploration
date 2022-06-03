

def reverse_number(x: int) -> int:
    is_negative = x < 0
    absolute_x = abs(x)
    x_str = str(absolute_x)
    x_str = x_str[::-1]
    new_x = int(x_str)

    if is_negative:
        new_x = -new_x

    limit = 2**31

    if -limit <= new_x <= (limit - 1):
        return new_x

    return 0


def main() -> None:
    print(reverse_number(-123))


if __name__ == "__main__":
    main()
