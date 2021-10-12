"""
Shifting right a number while discarding the right digit can be done by
integer division with 10.

12345 // 10 = 1234
"""

if __name__ == '__main__':
    a = 12345
    x = a // 10
    print(f"{a} -> {x}")
