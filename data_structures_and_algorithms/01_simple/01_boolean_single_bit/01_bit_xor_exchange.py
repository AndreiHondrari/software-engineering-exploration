

if __name__ == '__main__':
    a = True
    b = False

    print(f"BEFORE: a {a} b {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"AFTER: a {a} b {b}")
