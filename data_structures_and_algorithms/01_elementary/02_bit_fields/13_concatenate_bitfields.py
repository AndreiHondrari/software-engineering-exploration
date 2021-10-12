

if __name__ == '__main__':
    a = 0b10001000
    b = 0b11110011

    c = (a << 8) | b

    print(f"a {a:#0{10}b}")
    print(f"b {b:#0{10}b}")
    print(f"c {c:#0{18}b}")
