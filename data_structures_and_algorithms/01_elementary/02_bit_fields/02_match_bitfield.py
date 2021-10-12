"""
Detect a specific bit field. Flag detection.
"""


if __name__ == '__main__':
    # define inputs
    a = 0b01
    b = 0b10

    # define a reference/flag for matching
    REFERENCE = 0b01

    # detect
    x: bool = a & REFERENCE != 0b00
    y: bool = b & REFERENCE != 0b00

    print(f"x {x}")
    print(f"y {y}")
