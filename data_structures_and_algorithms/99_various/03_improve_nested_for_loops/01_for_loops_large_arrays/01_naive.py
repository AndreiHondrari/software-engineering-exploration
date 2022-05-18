import time
import random as rd
from typing import List


def process_lists(
    v1: List[int],
    v2: List[int]
) -> List[int]:

    out: List[int] = []

    for x in v1:
        for y in v2:
            if x == y:
                out.append(x)

    return out


def main() -> None:
    '''
    Notice we are running only with 10_000 and it still takes about 3 seconds
    '''

    print("Generate v1 ...")
    v1 = [rd.randint(0, 100) for _ in range(10_000)]

    print("Generate v2 ...")
    v2 = [rd.randint(0, 100) for _ in range(10_000)]

    print("Process v1, v2 ...")
    start = time.time()
    v3 = process_lists(v1, v2)
    stop = time.time()

    print(len(v3))

    print(f"Elapsed {stop-start:.2f} seconds")


if __name__ == "__main__":
    main()
