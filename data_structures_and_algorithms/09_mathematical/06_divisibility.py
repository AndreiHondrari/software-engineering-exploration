
def is_divisible_by(n: int, divisor: int) -> bool:
    return n % divisor == 0


if __name__ == '__main__':
    numbers = [
        2, 3, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    ]

    for n in numbers:
        div_2 = int(is_divisible_by(n, 2))
        div_3 = int(is_divisible_by(n, 3))
        div_5 = int(is_divisible_by(n, 5))
        print(f"{n: <4}: [2] {div_2} [3] {div_3} [5] {div_5}")
