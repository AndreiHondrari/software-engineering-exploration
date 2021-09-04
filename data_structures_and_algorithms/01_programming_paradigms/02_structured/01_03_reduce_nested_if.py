
if __name__ == '__main__':

    print("Nested blocks: False, False")
    condition1 = False
    condition2 = False
    if (condition1):
        if (condition2):
            print(f"INSTRUCTION")

    print("Nested blocks: False, True")
    condition1 = False
    condition2 = True
    if (condition1):
        if (condition2):
            print(f"INSTRUCTION")

    print("Nested blocks: True, False")
    condition1 = True
    condition2 = False
    if (condition1):
        if (condition2):
            print(f"INSTRUCTION")

    print("Nested blocks: True, True")
    condition1 = True
    condition2 = True
    if (condition1):
        if (condition2):
            print(f"INSTRUCTION")

    print("Reduced blocks: False, False")
    condition1 = False
    condition2 = False
    if (condition1 and condition2):
        print("INSTRUCTION")

    print("Reduced blocks: False, True")
    condition1 = False
    condition2 = True
    if (condition1 and condition2):
        print("INSTRUCTION")

    print("Reduced blocks: True, False")
    condition1 = True
    condition2 = False
    if (condition1 and condition2):
        print("INSTRUCTION")

    print("Reduced blocks: True, True")
    condition1 = True
    condition2 = True
    if (condition1 and condition2):
        print("INSTRUCTION")
