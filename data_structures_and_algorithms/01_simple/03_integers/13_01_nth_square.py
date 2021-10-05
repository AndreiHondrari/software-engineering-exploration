
def nth_square(n: int) -> int:
    return n**2


if __name__ == '__main__':
    for x in range(1, 10+1):
        val = nth_square(x)
        print(f"{x} -> {val}")
