

if __name__ == '__main__':

    a = 123456789
    DIGIT_COUNT = 9
    amount = 3
    x = a // 10**(DIGIT_COUNT - amount)
    print(f"{a} [{amount}] -> {x}")
