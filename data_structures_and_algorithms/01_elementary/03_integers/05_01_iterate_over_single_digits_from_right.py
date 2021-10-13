"""
Eliminate digits from the right side incrementally and then just take
the last digit as a remainder to the integer division with 10.


123456789 -> 9
12345678 -> 8
1234567 -> 7
...
"""

if __name__ == '__main__':
    x = 123456789

    # count digits
    total_digit_count: int = 0 if x > 0 else 1
    n_copy: int = x
    while n_copy > 0:
        total_digit_count += 1
        n_copy = n_copy // 10

    for i in range(total_digit_count):
        y = x // 10**i % 10
        print(y)
