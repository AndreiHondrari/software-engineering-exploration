import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Checks if a number is not prime by looking at:
    - if it is 1
    - if it is a multiple of two
    - if it is a perfect square
    - if the integer values smaller than the square root of our number are
      factors of our number

    If all those conditions are passed, then our number is prime.
    """

    if any([
        # 1 is not a prime
        n == 1,

        # no prime number is even, except from 2
        n > 2 and n % 2 == 0,
    ]):
        return False

    root = math.sqrt(n)

    # numbers that are perfect squares are not prime
    # since they are divided by some integral factor
    if (root * 10) % 10 != 0:
        # since our number is not a perfect square
        # it also means that it is the product of some imperfect square
        # k * k, where K belongs to the real numbers set.
        # we can check for potential factors that are smaller than
        # the root of our number, since any number that is equal to the root
        # would mean that its product would result in our number, and it would
        # make it a prime, or if k is bigger than the root, then the resulting
        # product would be greater than our number, hence we are not
        # interested in those values.
        for k in range(2, int(root)):
            if n % k == 0:
                return False
    else:
        return False

    return True


def make_primes(limit: int) -> List[int]:
    """
    Generate a list of primes from 2 to limit by doing trial
    evaluation of the numbers.

    This method is faster than the Sieve of Eratosthenes due to:
    - ose of a less nested for-looping
    - use of a very small range (0 to square root of the value)
    - use of preconditions that filter out obvious non-primes
      (1, even numbers, perfect squares)
    """
    primes: List[int] = []
    for n in range(2, limit+1):
        if is_prime(n):
            primes.append(n)
    return primes


if __name__ == '__main__':
    primes = make_primes(250_000)
    for p in primes:
        print(p)
