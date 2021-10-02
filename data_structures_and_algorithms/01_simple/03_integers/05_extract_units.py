
def get_unit(n: int) -> int:
    return n % 10


if __name__ == '__main__':
    numbers = [
        3, 5, 7,
        12, 15, 16, 17,
        521, 463, 659,
    ]

    for n in numbers:
        unit = get_unit(n)
        print(f"{n}'s unit: {unit}")
