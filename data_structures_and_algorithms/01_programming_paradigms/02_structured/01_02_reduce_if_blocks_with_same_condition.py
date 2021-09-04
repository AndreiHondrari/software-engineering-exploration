
if __name__ == '__main__':

    condition: bool = False

    print("Two blocks when false")
    if (condition):
        print("Instruction 1")

    if (condition):
        print("Instruction 2")

    print("\nTwo blocks when true")
    condition = True
    if (condition):
        print("Instruction 1")

    if (condition):
        print("Instruction 2")

    print("\nOne block when false")
    condition = False
    if (condition):
        print("Instruction 1")
        print("Instruction 2")

    print("\nOne block when true")
    condition = True
    if (condition):
        print("Instruction 1")
        print("Instruction 2")
