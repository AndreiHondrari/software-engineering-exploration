from typing import List


def get_squares(limit: int) -> List[int]:
    x = 0
    squares: List[int] = []
    for i in range(1, limit + 1):
        previous = x
        x = previous + i*2 - 1
        squares.append(x)

    return squares


if __name__ == '__main__':
    squares = get_squares(10)
    for n in squares:
        print(n, end=" ")
