"""
A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

---

"""
from time import time
from typing import Tuple


def is_palindrome(n: int) -> bool:
    # count digits
    digit_count = 0
    n_copy = n
    while n_copy > 0:
        digit_count += 1
        n_copy //= 10

    # detect palindromeness
    while n > 1:
        p = 10 ** (digit_count - 1)
        np = n // p
        nq = n % 10

        if np != nq:
            return False

        n = (n - np * p) // 10
        digit_count -= 2

    return True


def get_result_v1(digit_size: int) -> Tuple[int, int, int]:
    """
    Naive version.

    digit size over 3 will yield a very long run
    """
    assert digit_size <= 3, "Too large digit size, will be slow"

    # get max
    max_val = 0
    for i in range(digit_size):
        max_val += 10 ** i * 9

    # find largest palindrome
    largest_palindrome = 0
    min_val = 10 ** (digit_size - 1)
    selected_i = min_val
    selected_j = selected_i + 1
    for i in range(min_val, max_val + 1):
        for j in range(i + 1, max_val + 1):
            x = i * j
            if is_palindrome(x) and x > largest_palindrome:
                largest_palindrome = x
                selected_i = i
                selected_j = j

    return largest_palindrome, selected_i, selected_j


def get_result_v2(digit_size: int) -> Tuple[int, int, int]:
    """
    Enhanced version. Counts from the end backwards.
    Skips products smaller than the current palindrome.
    """

    # get max
    max_val = 0
    for k in range(digit_size):
        max_val += 10 ** k * 9

    # find largest palindrome
    largest_palindrome = 0
    min_val = 10 ** (digit_size - 1)
    selected_i = max_val
    selected_j = selected_i - 1
    for i in range(max_val, min_val - 1, -1):
        for j in range(i - 1, min_val - 1, -1):
            x = i * j

            if x <= largest_palindrome:
                break

            if is_palindrome(x):
                largest_palindrome = x
                selected_i = i
                selected_j = j

    return largest_palindrome, selected_i, selected_j


def get_result_v3(digit_size: int) -> Tuple[int, int, int]:
    """
    Should probably do:
    Find pattern amongst palindromes and their factors.
    99x91=9009
    96x88=8448

    99x83=8217
    99x82=8118
    99x81=8019

    91x88=8008
    99x73=7227

    99x64=6336
    99x55=5445
    99x46=4554
    99x37=3663
    99x28=2772
    99x19=1881
    97x55=5335
    96x66=6336
    96x44=4224
    96x22=2112
    95x55=5225
    94x64=6016
    93x55=5115
    91x77=7007
    91x66=6006
    91x55=5005
    91x44=4004
    91x33=3003
    91x22=2002
    91x11=1001
    89x11=979
    88x77=6776
    88x72=6336
    88x53=4664
    88x48=4224
    88x34=2992
    88x29=2552
    88x24=2112
    85x59=5015
    84x33=2772


    """
    pass


if __name__ == '__main__':

    # v1
    a = time()
    result, x, y = get_result_v1(2)
    b = time()
    print(f"R1: {x}x{y}={result} [{b-a:.2f}s]")

    a = time()
    result, x, y = get_result_v1(3)
    b = time()
    print(f"R2: {x}x{y}={result} [{b-a:.2f}s]")

    # v2
    a = time()
    result, x, y = get_result_v2(2)
    b = time()
    print(f"R3: {x}x{y}={result} [{b-a:.2f}s]")

    a = time()
    result, x, y = get_result_v2(3)
    b = time()
    print(f"R4: {x}x{y}={result} [{b-a:.2f}s]")

    a = time()
    result, x, y = get_result_v2(4)
    b = time()
    print(f"R5: {x}x{y}={result} [{b-a:.2f}s]")

    a = time()
    result, x, y = get_result_v2(5)
    b = time()
    print(f"R6: {x}x{y}={result} [{b-a:.2f}s]")
