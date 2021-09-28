"""
Invert all bits
"""


if __name__ == '__main__':
    a = 0b11001010
    print(f"INITIAL {a:#0{10}b}")

    a = a ^ 0xff
    print(f"FINAL   {a:#0{10}b}")
