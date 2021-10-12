"""
Fill bits to the right from position
"""

if __name__ == '__main__':
    x = 0x00
    position = 5
    number_of_bits = 3

    for i in range(number_of_bits):
        x = x | (
            0b1 << (position - i)
        )

    print(f"{x:#0{10}b}")
