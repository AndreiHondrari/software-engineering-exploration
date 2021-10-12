"""
We can force the n-th digit to 0 by combining the following:
- we extract the digits right to that as one result
- we cancel all digits from the n-th position to the right as a second result
- we add up the previous results

Cancelling the digits can be done in two ways:
- by subtracting the undesired digits
- by integer division and remultiplication with 10 to the power of offset + 1

Let's assume our number is 45678

Scenario 1:
45678 - (45678 - 45678 % 1000) + (45678 % 100)
45678 - 678 + 78 = 45078

Scenario 2:
(45678 // 1000) * 1000 + 45678 % 100
45 * 1000 + 78 = 45078
"""

if __name__ == '__main__':

    a: int = 12345
    offset: int = 2
    x: int = a - (a % 10**(offset + 1)) + (a % 10**offset)
    y: int = (a // 10**(offset + 1)) * 10**(offset + 1) + (a % 10**offset)

    print(f"v1 {a} -> {x}")
    print(f"v2 {a} -> {y}")
