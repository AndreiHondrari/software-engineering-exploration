

if __name__ == '__main__':
    a = 0b00001001
    b = 0b11000011
    x = a | b

    print(f"a         {a:#0{10}b}")
    print(f"b         {b:#0{10}b}")
    print(f"x (a | b) {x:#0{10}b}")
