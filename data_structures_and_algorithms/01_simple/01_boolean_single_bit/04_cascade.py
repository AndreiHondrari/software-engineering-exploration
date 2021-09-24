

if __name__ == '__main__':

    a = True
    b = True

    for i in range(6):

        if a:
            # stage 1
            print("A")
            a = False
        elif b:
            # stage 2
            print("B")
            b = False
        else:
            # last stage and reset
            a = True
            b = True
            print("LAST")

    print("DONE")
