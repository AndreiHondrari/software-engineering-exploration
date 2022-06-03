"""
Calculating the exponent of a number in a base according to the formula:

           log   (x)
               k
log   (x) = -------
    b      log   (b)
               k

For which we don't care what k is, for what we care it can be 'e'.
"""
import math


if __name__ == '__main__':
    base = 2
    number = 8

    numerator_log = math.log(number)
    denominator_log = math.log(base)

    exponent = numerator_log / denominator_log

    print(f"{base} ** {exponent} = {number}")
