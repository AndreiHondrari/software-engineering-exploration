"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

---

"""
from time import time


def get_result_v1(n: int) -> int:
    factor = 2
    largest_factor = 1

    while n > 1:
        if n % factor == 0:
            largest_factor = factor
            n = int(n / factor)

            # continue dividing until you can't
            while n % largest_factor == 0:
                n = int(n / largest_factor)

        factor += 1

    return largest_factor


if __name__ == '__main__':
    N = 600_851_475_143

    # v1
    a = time()
    result = get_result_v1(N)
    b = time()
    print(f"R1: {result} [{b-a:.2f}s]")
