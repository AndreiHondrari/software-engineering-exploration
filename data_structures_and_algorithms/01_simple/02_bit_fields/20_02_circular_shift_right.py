

if __name__ == '__main__':
    # assume the input is 1 byte
    x = 0xf0
    print(f"INITIAL {x:#0{10}b}")

    N = 3
    shift_amount = N % 8

    # obtain left part by shifting completely to the left by 8 bits
    # and then just offset by the desired shift amount
    # and mask to be sure it's 1 byte
    left_part = (x << (8 - shift_amount)) & 0xff

    # obtain right part by shifting for the necessary amount of bits
    right_part = x >> shift_amount

    # recombine left and right into the final result
    x = left_part | right_part
    print(f"FINAL   {x:#0{10}b}")
