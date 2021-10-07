import math


if __name__ == '__main__':
    base = 2
    number = 8

    exponent = math.floor(math.log(number, base))

    print(f"{base} ** {exponent} = {number}")
