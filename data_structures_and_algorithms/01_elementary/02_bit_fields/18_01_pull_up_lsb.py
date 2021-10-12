"""
Pull up least significant bit
"""

if __name__ == '__main__':
    a = 0x00
    print(f"INITIAL {a:#0{10}b}")

    a = a | 0b1
    print(f"FINAL   {a:#0{10}b}")
