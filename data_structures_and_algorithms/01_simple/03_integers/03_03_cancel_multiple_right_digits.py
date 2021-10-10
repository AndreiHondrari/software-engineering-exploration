

if __name__ == '__main__':

    a: int = 123456789
    amount: int = 4
    x = a - a % 10**amount
    print(f"{a} -> {x}")
