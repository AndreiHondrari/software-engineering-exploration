"""
In order to extract the n-th digit counting from right we must combine
the following operations:

Scenario 1:
- extract multiple numbers from the left side, with our target digit
being the least significant digit (unit) in our result
- obtain the remainder of the integer division of the number resulted in
the previous step and 10

Scenario 2:
- extract multiple digits from the right side, in which the resulting number
has our target digit as the most significant digit, discarding basically
the digits left to that
- extract the most significant digit
"""

if __name__ == '__main__':
    a: int = 123456789
    offset = 3

    x: int = a // 10**offset % 10
    y: int = (a % 10**(offset + 1)) // 10**offset

    # counting from 0 of course
    print(f"digit #{offset} from {a}")
    print(f"x: {x}")
    print(f"y: {y}")
