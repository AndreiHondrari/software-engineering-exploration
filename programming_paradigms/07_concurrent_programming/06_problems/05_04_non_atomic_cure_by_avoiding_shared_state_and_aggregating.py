"""
In order to protect against undetermined behaviour while using
non-atomic operators, one could avoid global state alltogether.
"""

import threading
import multiprocessing as mp

from multiprocessing.connection import Connection


def do_inc(
    result_connection: Connection,
    target: int
) -> None:

    local_k = 0
    for _ in range(target):
        local_k += 1

    result_connection.send(local_k)


def main() -> None:
    NO_OF_THREADS = 10
    TARGET = 1_000_000

    print("create threads")
    threads = []
    result_connections = []
    for _ in range(NO_OF_THREADS):
        receiver_connection, sender_connection = mp.Pipe(duplex=False)
        result_connections.append(receiver_connection)

        new_thread = threading.Thread(
            target=do_inc,
            args=(sender_connection, TARGET,)
        )
        new_thread.daemon = True
        threads.append(new_thread)

    print("start threads")
    for t in threads:
        t.start()

    print("wait for threads to DIE ...")
    for t in threads:
        t.join()

    # check results
    k = 0
    for conn in result_connections:
        k += conn.recv()

    EXPECTED = NO_OF_THREADS * TARGET
    result = k == EXPECTED
    print(f"CHECK {k} == {EXPECTED} ? : {result}")


if __name__ == '__main__':
    main()
