"""
Shift bits
"""

if __name__ == '__main__':
    a = 0b00011000
    x = a << 1
    y = a >> 2

    print(f"a          {a:#0{10}b}")
    print(f"x (a << 1) {x:#0{10}b}")
    print(f"y (a >> 2) {y:#0{10}b}")
