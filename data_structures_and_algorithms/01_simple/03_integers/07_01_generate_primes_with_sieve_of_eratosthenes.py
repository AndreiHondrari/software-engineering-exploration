from typing import List


def make_primes(limit: int) -> List[int]:
    primes: List[int] = []
    mark_list = [False for _ in range(limit + 1)]
    for i in range(2, limit + 1):

        # if our number has been marked as a multiple
        # of a previous number, then it means that
        # n is divisible by that previous number, hence n is not prime
        is_n_marked: bool = mark_list[i]
        if is_n_marked:
            continue

        # classify our n as prime
        primes.append(i)

        # cross out all multiples of n
        for j in range(i+1, limit + 1):
            # skip marked numbers
            is_subsequent_n_marked: bool = mark_list[j]
            if is_subsequent_n_marked:
                continue

            # detect forward multiple
            if j % i == 0:
                mark_list[j] = True  # mark it as a multiple of n

    return primes


if __name__ == '__main__':
    primes = make_primes(20_000)
    for p in primes:
        print(p)
