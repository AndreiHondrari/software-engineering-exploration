

if __name__ == '__main__':
    a = 0b00001001
    b = 0b11000011

    # mask that select the bits from b
    MASK = 0x0F

    x = a | (b & MASK)

    print(f"a {a:#0{10}b}")
    print(f"b {b:#0{10}b}")
    print(f"m {MASK:#0{10}b}")
    print(f"x {x:#0{10}b}")
