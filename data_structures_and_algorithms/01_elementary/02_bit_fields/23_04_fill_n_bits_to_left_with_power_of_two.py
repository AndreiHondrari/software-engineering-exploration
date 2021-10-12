"""
Fill bits to the left from position
"""

if __name__ == '__main__':
    position = 2
    number_of_bits = 3

    x = (2**number_of_bits - 1) << position

    print(f"{x:#0{10}b}")
