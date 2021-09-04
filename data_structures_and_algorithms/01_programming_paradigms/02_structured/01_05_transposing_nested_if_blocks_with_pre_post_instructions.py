

if __name__ == '__main__':

    ALWAYS_TRUE: bool = True
    variable_condition: bool = False

    print("Nested with false")
    if (ALWAYS_TRUE):
        print("Pre instruction")

        if (variable_condition):
            print("Infix instruction")

        print("Post instruction")

    print("\nNested with true")
    variable_condition = True
    if (ALWAYS_TRUE):
        print("Pre instruction")

        if (variable_condition):
            print("Infix instruction")

        print("Post instruction")

    print("\nFlattened with false")
    variable_condition = False
    if (ALWAYS_TRUE):
        print("Pre instruction")

    if (ALWAYS_TRUE and variable_condition):
        print("Infix instruction")

    if (ALWAYS_TRUE):
        print("Post instruction")

    print("\nFlattened with true")
    variable_condition = True
    if (ALWAYS_TRUE):
        print("Pre instruction")

    if (ALWAYS_TRUE and variable_condition):
        print("Infix instruction")

    if (ALWAYS_TRUE):
        print("Post instruction")
