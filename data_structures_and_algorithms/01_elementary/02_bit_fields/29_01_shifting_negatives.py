

if __name__ == '__main__':
    a = 0x0f
    b = -0x0f

    print("INITIAL VALUES")
    print(f"a        {a:0{8}b} {a: >3}")
    print(f"b        {b:0{8}b} {b: >3}")
    print(f"b masked {b & 0xff:0{8}b}")

    # shift a few places

    a = a >> 2
    b = b >> 2

    print("\nSHIFTED A FEW PLACES")
    print(f"a        {a:0{8}b} {a: >3}")
    print(f"b        {b:0{8}b} {b: >3}")
    print(f"b masked {b & 0xff:0{8}b}")

    # shift fully

    a = a >> 6
    b = b >> 6

    print("\nSHIFTED FULLY")
    print(f"a        {a:0{8}b} {a: >3}")
    print(f"b        {b:0{8}b} {b: >3}")
    print(f"b masked {b & 0xff:0{8}b}")

    # shift extra

    a = a >> 1
    b = b >> 1

    print("\nSHIFTED EXTRA")
    print(f"a        {a:0{8}b} {a: >3}")
    print(f"b        {b:0{8}b} {b: >3}")
    print(f"b masked {b & 0xff:0{8}b}")
