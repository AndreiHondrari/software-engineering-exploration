

if __name__ == '__main__':

    print("Original when true")
    if True:
        print("Instruction 1")
    else:
        print("Instruction 2")

    print("\nOriginal when false")
    if False:
        print("Instruction 1")
    else:
        print("Instruction 2")

    print("\nInverted when true")
    if True:
        print("Instruction 2")
    else:
        print("Instruction 1")

    print("\nInverted when false")
    if False:
        print("Instruction 2")
    else:
        print("Instruction 1")
