"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

---
First way is to do a forloop from 3 to 1000 and add up those
dividible by 3 or 5.

---
Second way is to think mathematically.
between 0 and 1000, you have the following series

for 3 you have 3 + 6 + 9 + 12 + ... + 999
for 5 you have 5 + 10 + 15 + ... + 995

factor

3 * (1 + 2 + 3 + ... + 333)
5 * (1 + 2 + 3 + ... + 195)

there is a pattern, some series, where if we look at the last element:
333 = 999/3
195 = 995/5

generally like: p = last_number_dividible / n , where
p: our series last term
n: our smallest factor

our series would be:
(p * (1 + p)) / 2

so our result will be:
n * (
    (p * (1 + p))
        / 2
)
"""
from time import time


def get_result_v1(limit: int) -> int:
    result = 0
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


def sum_divisible_by(n: int, target: int) -> int:
    # find last term
    last_term = target
    for x in range(target - 1, n - 1, -1):
        if x % n == 0:
            last_term = x
            break

    # calculate
    p = last_term / n
    return int(n * ((p * (1 + p)) / 2))


def get_result_v2(limit: int) -> int:
    result_for_3 = sum_divisible_by(3, limit)
    result_for_5 = sum_divisible_by(5, limit)

    # get rid of the surplus where a number is divisible by both 3 and 5
    # essentially getting rid of the duplicate surplus
    result_for_15 = sum_divisible_by(15, limit)
    return result_for_3 + result_for_5 - result_for_15


if __name__ == '__main__':
    N = 1000
    BIG_N = 10_000_000

    a = time()
    result = get_result_v1(N)
    b = time()
    print(f"R1: {result} [{b-a:.2f}s]")

    a = time()
    result = get_result_v1(BIG_N)
    b = time()
    print(f"R2: {result} [{b-a:.2f}s]")

    a = time()
    result = get_result_v2(N)
    b = time()
    print(f"R3: {result} [{b-a:.2f}s]")

    a = time()
    result = get_result_v2(BIG_N)
    b = time()
    print(f"R4: {result} [{b-a:.2f}s]")
