
import functools
import time
from typing import Generator
from collections import deque

hprint = functools.partial(print, '-' * 20)


def do_something(name: str, no_iterations: int) -> Generator[None, int, None]:
    for i in range(no_iterations):
        print(f"do_something [{name}]")
        yield


def main() -> None:
    some1 = do_something("aaa", 2)
    some2 = do_something("bbb", 4)

    task_queue = deque()

    task_queue.append(some1)
    task_queue.append(some2)

    i = 0
    while len(task_queue) > 0:
        print("step", i)

        task = task_queue.popleft()
        try:
            next(task)
            task_queue.append(task)
        except StopIteration:
            print("task done")

        time.sleep(0.05)
        i += 1

    print("-- FIN --")


if __name__ == "__main__":
    main()
