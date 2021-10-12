

if __name__ == '__main__':
    a = 0b00010011
    b = 0b01011100

    # the mask is specifically designed for the flag
    # especially useful in applications like
    # IP address subnet detection
    FLAG = 0b01010000
    MASK = 0b11110000

    x: bool = (a & MASK) == FLAG
    y: bool = (b & MASK) == FLAG

    print(f"A {a:#0{10}b}")
    print(f"X {x}")
    print(f"Y {y}")
