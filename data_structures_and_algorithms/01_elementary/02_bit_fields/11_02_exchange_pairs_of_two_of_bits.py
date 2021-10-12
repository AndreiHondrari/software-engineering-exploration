

if __name__ == '__main__':
    a = 0b00111100
    # 0x33 and 0xcc are opposite masks
    # 0x33 = 0b00110011
    # 0xcc = 0b11001100
    x = (a & 0x33) << 2 | (a & 0xcc) >> 2
    y = (a & 0x33) << 2 | (a & (0x33 ^ 0xff)) >> 2
    z = (a & (0xcc ^ 0xff)) << 2 | (a & 0xcc) >> 2

    print(f"BEFORE {a:#0{10}b}")
    print(f"AFTER1 {x:#0{10}b}")
    print(f"AFTER2 {y:#0{10}b}")
    print(f"AFTER3 {z:#0{10}b}")
