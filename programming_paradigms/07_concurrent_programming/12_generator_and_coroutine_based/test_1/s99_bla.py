
import string
import random as rd
import time
import threading as th
import multiprocessing as mp

from collections import deque


def do_io_operations(
    data_stream: mp.Queue,
    io_ready_event: mp.Event,
    no_lines: int
):
    this_thread = th.current_thread()

    print(f"[{this_thread.name}] START")

    # perform some IO operations
    for i in range(no_lines):
        value = rd.sample(string.ascii_letters, 1)[0]
        print(f"[{this_thread.name}] obtained '{value}'")

        time.sleep(rd.random() * 0.8 + 0.2)

        print(f"[{this_thread.name}] passing '{value}' ...")
        data_stream.put(value)

    # mark the IO operation as complete
    io_ready_event.set()

    print(f"[{this_thread.name}] STOP")


def get_data(thread_name: str):
    # launch thread operations
    io_ready_event = mp.Event()
    data_stream = mp.Queue()
    io_thread = th.Thread(
        target=do_io_operations,
        name=thread_name,
        args=(data_stream, io_ready_event, 5)
    )

    io_thread.start()

    # await for IO operations to finish
    while not io_ready_event.is_set():
        yield

    # when IO is finished, copy data into buffer
    buffer = []

    while not data_stream.empty():
        value = data_stream.get_nowait()
        print("copy into buffer", value)
        buffer.append(value)

    # release buffer to caller
    return buffer


class EventLoop:

    def __init__(self):
        self.tasks = deque()

    def call_soon(self, task):
        self.tasks.append(task)

    def run(self):
        result = None
        # run the tasks in a round-robin fashion
        while self.tasks:
            task = self.tasks.popleft()

            try:
                next(task)
            except StopIteration:
                continue  # skip re-adding the task to queue

            self.tasks.append(task)

        return result


def async_main():
    promise_1 = get_data('io-thread-1')
    promise_2 = get_data('io-thread-2')


def main() -> None:
    print("START")

    loop = EventLoop()

    loop.




    # copy into buffer
    buffer = None
    while True:
        try:
            next(promise)
        except StopIteration as err:
            buffer = err.value
            break

    print(" \n\n", "-" * 10)
    print(buffer)

    # io_thread_2.start()

    # x = data_stream.empty()
    # print(x)
    # io_thread_1.join()

    print("DONE")


if __name__ == "__main__":
    main()
