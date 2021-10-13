"""
To extract the most significant digit of a number,
we must know beforehand the number of digits of the number.

We extract the digit by performing integer division of the number with
10 to the power of the amount of digits minus one.

Let's assume a number 5678 with 4 digits.
10 to the power of (4-1) = 1000

5678 // 1000 = 5
"""

if __name__ == '__main__':
    numbers = [
        5, 10, 17, 289
    ]

    for n in numbers:
        # count digits
        count: int = 0 if n > 0 else 1
        n_copy: int = n
        while n_copy > 0:
            n_copy = n_copy // 10
            count += 1

        # extract most significant digit
        result = n // 10**(count - 1)

        print(f"{n} -> {result}")
