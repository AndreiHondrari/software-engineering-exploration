

if __name__ == '__main__':
    a = 0b01101001
    # 0x55 and 0xaa are opposite masks
    # 0x55 = 0b01010101
    # 0xaa = 0b10101010
    x = (a & 0x55) << 1 | (a & 0xaa) >> 1
    y = (a & 0x55) << 1 | (a & (0x55 ^ 0xff)) >> 1
    z = (a & (0xaa ^ 0xff)) << 1 | (a & 0xaa) >> 1

    print(f"BEFORE {a:#0{10}b}")
    print(f"AFTER1 {x:#0{10}b}")
    print(f"AFTER2 {y:#0{10}b}")
    print(f"AFTER3 {z:#0{10}b}")
