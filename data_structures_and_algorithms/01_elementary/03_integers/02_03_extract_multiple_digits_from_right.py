"""
The remainder of a number and 10 to the power of k results in
k amount of digits from the right side of our number.

k = 2
10 to the power of k = 100
1579 % 100 = 79
"""

if __name__ == '__main__':

    a = 123456789
    amount = 4
    x = a % 10**amount
    print(f"{a} [{amount}] -> {x}")
