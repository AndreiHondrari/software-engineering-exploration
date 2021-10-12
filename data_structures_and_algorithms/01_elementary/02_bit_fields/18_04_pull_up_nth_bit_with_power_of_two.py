"""
Pull up nth bit
"""

if __name__ == '__main__':
    a = 0x00
    print(f"INITIAL {a:#0{10}b}")

    N = 3
    a = a | 2**N
    print(f"FINAL   {a:#0{10}b}")
