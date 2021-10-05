from typing import List


def get_squares(limit: int) -> List[int]:
    squares: List[int] = []

    for x in range(1, limit + 1):
        squares.append(x ** 2)

    return squares


if __name__ == '__main__':
    squares = get_squares(10)
    for n in squares:
        print(n, end=" ")
