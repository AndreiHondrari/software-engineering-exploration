"""
Cancel most significant bit
"""

if __name__ == '__main__':
    a = 0xff
    print(f"INITIAL {a:#0{10}b}")

    N = 3
    a = a & (0xff ^ (2**N))
    print(f"FINAL   {a:#0{10}b}")
