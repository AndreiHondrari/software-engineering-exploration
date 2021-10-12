"""
You would expect that 0.1 + 0.1 + 0.1 == 0.3

Rounding does not help.
"""

if __name__ == '__main__':
    # bad rounding
    print("BAD ROUNDING")
    x = round(0.1, 1) + round(0.1, 1) + round(0.1, 1)

    if (x == round(0.3, 1)):
        print("detected")
    else:
        print("ANTI-detected")

    # good rounding
    print("\nGOOD ROUNDING")
    x = round(0.1 + 0.1 + 0.1, 1)

    if (x == round(0.3, 1)):
        print("detected")
    else:
        print("ANTI-detected")
