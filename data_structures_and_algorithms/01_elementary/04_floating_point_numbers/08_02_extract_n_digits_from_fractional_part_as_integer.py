

if __name__ == '__main__':
    a: float = 0.7891234569999
    N_DIGITS: int = 3

    x: int = int(a * 10**N_DIGITS % 10**N_DIGITS)

    print(f"{a} -> {x}")
