a = 0
b = 1


def p() -> None:
    print(f"a: {a:0>1b} b: {b:0>1b}")


if __name__ == '__main__':
    p()
    a = a ^ b
    p()
    b = a ^ b
    p()
    a = a ^ b
    p()
