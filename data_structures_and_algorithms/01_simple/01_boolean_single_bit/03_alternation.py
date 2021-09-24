
if __name__ == '__main__':

    a = True

    for i in range(10):
        if a:
            print("this")
        else:
            print("that")
        a = not a
