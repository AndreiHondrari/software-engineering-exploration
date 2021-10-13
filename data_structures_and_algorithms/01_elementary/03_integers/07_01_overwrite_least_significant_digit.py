"""
Overwrite the least significant digit by canceling it first and then adding
the new digit to the number.

n = 444

Scenario 1:
(444 // 10) * 10 + 7
440 + 7 = 447

Scenario 2:
444 - 444 % 10 + 7
444 - 4 + 7 = 447

"""

if __name__ == '__main__':
    a: int = 55555
    new_digit: int = 7

    x: int = a // 10 * 10 + new_digit

    y: int = a - a % 10 + new_digit

    print(f"v1 {a} with {new_digit} -> {x}")
    print(f"v2 {a} with {new_digit} -> {y}")
