import math


def is_perfect_square(n: int) -> bool:
    """
    A number divided by its square root will always have 0 remainder.
    """
    root = math.sqrt(n)
    division_remainder = n % root
    return division_remainder == 0


if __name__ == '__main__':
    numbers = list(range(1, 20 + 1))
    for x in numbers:
        x_perfect: bool = is_perfect_square(x)
        print(f"{x}: {x_perfect}")
