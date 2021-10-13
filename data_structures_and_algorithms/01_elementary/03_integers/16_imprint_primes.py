"""
A product of prime numbers will not have remainders as a result of division
with one of its factors, but it will have remainders with other prime
numbers.
"""

if __name__ == '__main__':

    # define some prime numbers
    a: int = 3
    b: int = 5
    c: int = 23

    # imprint values onto the film
    d: int = 1
    d *= a
    d *= b
    d *= c

    res: bool = False

    ref = 7
    res = d % ref == 0
    print(f"{d} with {ref} -> {res}")

    ref = b
    res = d % ref == 0
    print(f"{d} with {ref} -> {res}")
