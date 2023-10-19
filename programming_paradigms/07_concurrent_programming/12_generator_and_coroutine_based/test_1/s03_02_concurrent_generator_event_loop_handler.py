"""
Concurrency with generators

Let's say we would like to run
111 do foo part 1
AAA do bar part 1
222 do foo part 2
BBB do bar part 2
333 do foo part 3
CCC do bar part 3

Run parts of the tasks until they are done.
"""

from collections import deque


class EventLoop:

    def __init__(self):
        self.tasks = deque()

    def call_soon(self, task):
        self.tasks.append(task)

    def run(self):
        # run the tasks in a round-robin fashion
        while self.tasks:
            task = self.tasks.popleft()

            try:
                x = next(task)
                print("step", x)
            except StopIteration as stop_iteration_err:
                print("result", stop_iteration_err.value)
                continue  # skip re-adding the task to queue

            self.tasks.append(task)


loop = EventLoop()


def do_foo():
    print("111")
    yield 444
    print("222")
    yield 555
    print("333")

    return 7777


def do_bar():
    print("AAA")
    yield "DDD"
    print("BBB")
    yield "EEE"
    print("CCC")

    return 9999


def main() -> None:
    # declare some tasks
    foo = do_foo()
    bar = do_bar()

    loop.call_soon(foo)
    loop.call_soon(bar)

    loop.run()

    print("\nDONE")


if __name__ == "__main__":
    main()
