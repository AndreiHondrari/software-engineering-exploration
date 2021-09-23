"""
The (similar x) means that the instruction is the same in both the
if and the else blocks. the x is there just to help us
identify from which block it was called.
"""


if __name__ == '__main__':

    print("Nested: False, False")
    condition1 = False
    condition2 = False
    if (condition1):
        if (not condition2):
            print("Instruction (similar 1)")
    else:
        if (condition2):
            print("Instruction (similar 2)")

    print("\nNested: False, True")
    condition1 = False
    condition2 = True
    if (condition1):
        if (not condition2):
            print("Instruction (similar 1)")
    else:
        if (condition2):
            print("Instruction (similar 2)")

    print("\nNested: True, False")
    condition1 = True
    condition2 = False
    if (condition1):
        if (not condition2):
            print("Instruction (similar 1)")
    else:
        if (condition2):
            print("Instruction (similar 2)")

    print("\nNested: True, True")
    condition1 = True
    condition2 = True
    if (condition1):
        if (not condition2):
            print("Instruction (similar 1)")
    else:
        if (condition2):
            print("Instruction (similar 2)")

    print("Reduced: False, False")
    condition1 = False
    condition2 = False
    if (condition1 ^ condition2):
        print("Instruction")

    print("\nReduced: False, True")
    condition1 = False
    condition2 = True
    if (condition1 ^ condition2):
        print("Instruction")

    print("\nReduced: True, False")
    condition1 = True
    condition2 = False
    if (condition1 ^ condition2):
        print("Instruction")

    print("\nReduced: True, True")
    condition1 = True
    condition2 = True
    if (condition1 ^ condition2):
        print("Instruction")
