"""
Extract a specific part of the bit field.
Also it cancels the other part of the representation by bringing all those
bits to 0.
"""

if __name__ == '__main__':

    # define our input 0101 0110
    a = 0b01010110

    # define the mask
    MASK = 0b11110000

    # extract the relevant information -> the 0101
    x = a & MASK

    print(f"{x:#0{10}b}")
