"""
In order to extract multiple digits left of the n-th digit counting from right,
we must combine the following operations:

Scenario 1:
- extract multiple numbers from the left side, with our target digits
being on the right in our result
- obtain the remainder of the integer division of the number resulted in
the previous step and 10 t o the power of the amount of required digits

Scenario 2:
- extract multiple digits from the right side, in which the resulting number
has our target digits on the left, discarding basically the digits left to that
- extract the required amount of digits from the left side of that result
"""

if __name__ == '__main__':
    a: int = 123456789
    offset = 3
    amount = 4

    x: int = a // 10**offset % 10**amount
    y: int = (a % 10**(offset + amount)) // 10**offset

    # counting from 0 of course
    print(f"{amount} digits from #{offset} from {a}")
    print(f"x: {x}")
    print(f"y: {y}")
