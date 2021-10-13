"""
Pass digits from the left side by incrementally eliminating all
the digits to the right, and then using the result to obtain a
remainder from the integer division with 10.

1 -> 1
12 -> 2
123 -> 3
...
"""

if __name__ == '__main__':
    x = 123456789

    # count digits
    total_digits_count: int = 0 if x > 0 else 1
    n_copy: int = x
    while n_copy > 0:
        total_digits_count += 1
        n_copy = n_copy // 10

    for i in range(total_digits_count):
        y = (x // 10**(total_digits_count - i - 1)) % 10
        print(y)
