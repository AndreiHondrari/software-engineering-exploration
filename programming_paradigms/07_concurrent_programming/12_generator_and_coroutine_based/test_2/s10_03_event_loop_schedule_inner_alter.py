
import functools
import time
from typing import Generator
from collections import deque

hprint = functools.partial(print, '-' * 20)

# NOTICE task queue exists at a top level
task_queue = deque()


def do_foo():
    yield
    print("DO_FOO")


def do_something() -> Generator[None, int, None]:
    yield
    print("DO_SOME")
    foo = do_foo()
    next(foo)
    task_queue.append(foo)


def main() -> None:
    some = do_something()
    next(some)
    task_queue.append(some)

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
