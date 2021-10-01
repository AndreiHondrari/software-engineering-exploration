

def is_palindrome(n: int) -> bool:
    left_nibble = n & 0xf0
    right_nibble = n & 0x0f

    reversed_left_nibble = (
        ((left_nibble & 0x55) << 1) |
        ((left_nibble & 0xaa) >> 1)
    )

    reversed_left_nibble = (
        ((reversed_left_nibble & 0x33) << 2) |
        ((reversed_left_nibble & 0xcc) >> 2)
    )

    reversed_left_nibble = (
        ((reversed_left_nibble & 0x0f) << 4) |
        ((reversed_left_nibble & 0xf0) >> 4)
    )

    return (reversed_left_nibble & right_nibble) != 0


if __name__ == '__main__':
    a = 0b10001010
    b = 0b10011001
    c = 0b11000011

    print(f"{a:#0{10}b}: {is_palindrome(a)}")
    print(f"{b:#0{10}b}: {is_palindrome(b)}")
    print(f"{c:#0{10}b}: {is_palindrome(c)}")
