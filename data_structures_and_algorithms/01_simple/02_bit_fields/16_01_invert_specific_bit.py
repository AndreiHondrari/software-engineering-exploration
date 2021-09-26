

if __name__ == '__main__':
    a = 0b11110000
    print(f"INITIAL    {a:#0{10}b}")

    N1 = 2
    N2 = 5

    # invert the nth bit
    x = a ^ (0b1 << N1)
    y = a ^ (0b1 << N2)

    print(f"FINAL AT {N1} {x:#0{10}b}")
    print(f"FINAL AT {N2} {y:#0{10}b}")
