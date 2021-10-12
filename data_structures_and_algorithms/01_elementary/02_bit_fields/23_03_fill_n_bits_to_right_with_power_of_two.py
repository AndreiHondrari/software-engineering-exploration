"""
Fill bits to the right from position
"""

if __name__ == '__main__':
    position = 5
    number_of_bits = 3

    x = (2**number_of_bits - 1) << (position - number_of_bits + 1)

    print(f"{x:#0{10}b}")
