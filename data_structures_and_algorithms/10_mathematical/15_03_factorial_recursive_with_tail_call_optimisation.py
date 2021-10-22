"""
Python doesn't have tail call optimisation,
but if it were a language that supported that,
this would be an alternative recursive implementation
that would ensure no stack-overflow can happen
and speed-up the return of the function
"""


def factorial(n: int, product: int = 1) -> int:
    assert n >= 0, "value must be zero or positive"

    if n <= 1:
        return product

    return factorial(n - 1, n * product)


if __name__ == '__main__':
    for k in range(10 + 1):
        result = factorial(k)
        print(f"{k}! = {result}")
