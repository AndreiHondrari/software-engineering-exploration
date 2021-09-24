

if __name__ == '__main__':
    a = True
    b = False

    print(f"[BEFORE] a {a} b {b}")
    c = a
    a = b
    b = c
    print(f"[AFTER] a {a} b {b}")
