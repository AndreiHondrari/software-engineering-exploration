
if __name__ == '__main__':

    ALWAYS_TRUE: bool = True

    print("Nested with False")
    variable_condition: bool = False
    if (ALWAYS_TRUE):
        if (variable_condition):
            print("Instruction 1")
        else:
            print("Instruction 2")

    print("\nNested with True")
    variable_condition = True
    if (ALWAYS_TRUE):
        if (variable_condition):
            print("Instruction 1")
        else:
            print("Instruction 2")

    print("\nReduced with False")
    variable_condition = False
    if (ALWAYS_TRUE and variable_condition):
        print("Instruction 1")

    if (ALWAYS_TRUE and not variable_condition):
        print("Instruction 2")

    print("\nReduced with True")
    variable_condition = True
    if (ALWAYS_TRUE and variable_condition):
        print("Instruction 1")

    if (ALWAYS_TRUE and not variable_condition):
        print("Instruction 2")
