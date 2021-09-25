"""
Alternate bits
"""

if __name__ == '__main__':
    x = 0b0

    state = 0b0
    for i in range(8):
        # alternate
        if state == 0b0:
            state = 0b1
        else:
            state = 0b0

        # write on spot
        x = x | (state << i)

    print(f"{x:#0{10}b}")
