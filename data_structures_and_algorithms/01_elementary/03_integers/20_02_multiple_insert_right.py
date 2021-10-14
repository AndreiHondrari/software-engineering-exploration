from typing import List


if __name__ == '__main__':
    a: int = 1234
    new_digits: List[int] = [
        9, 4, 8, 5, 7,
    ]

    x: int = a
    for d in new_digits:
        x = x * 10 + d

    print(f"{a} with {new_digits} -> {x}")
