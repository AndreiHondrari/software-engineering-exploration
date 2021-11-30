"""
Lock convoy

If there is a hot lock that has to be acquired and released very frequent,
a large number of threads competing to acquire the lock will actually
slow down the overall execution and/or create a bottleneck for a queue
of incoming requests.
"""
import time
import threading
import multiprocessing

from typing import List
from multiprocessing.connection import Connection


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def do_something(
    stop_event: threading.Event,
    lock: threading.Lock,
    result_connection: Connection
) -> None:

    count = 0
    while not stop_event.is_set():
        lock.acquire()
        count += 1
        lock.release()

    result_connection.send(count)


def launch_for(
    number_of_threads: int,
    duration: int,
    name: str
) -> None:
    print("", flush=True)
    tprint(f"Launch {name} | {number_of_threads} threads | {duration}s")
    stop_event = threading.Event()
    hot_lock = threading.Lock()

    result_connections: List[Connection] = []

    tprint(f"[{name}] create threads")
    threads: List[threading.Thread] = []

    for i in range(24):
        receiver_connection, sender_connection = multiprocessing.Pipe()
        result_connections.append(receiver_connection)

        new_thread = threading.Thread(
            target=do_something,
            args=(stop_event, hot_lock, sender_connection,)
        )
        new_thread.daemon = True
        threads.append(new_thread)

    tprint(f"[{name}] start threads")
    for t in threads:
        t.start()

    tprint(f"[{name}] wait for the threads")
    time.sleep(duration)

    tprint(f"[{name}] kill threads")
    stop_event.set()

    tprint(f"[{name}] wait for threads to DIE ...")
    for t in threads:
        t.join()

    final_count = 0
    for res_con in result_connections:
        final_count += res_con.recv()
    tprint(f"[{name}] final count: {final_count}")


def main() -> None:
    launch_for(4, 5, "ALFA")
    launch_for(24, 5, "BRAVO")
    launch_for(128, 5, "CHARLIE")


if __name__ == '__main__':
    main()
