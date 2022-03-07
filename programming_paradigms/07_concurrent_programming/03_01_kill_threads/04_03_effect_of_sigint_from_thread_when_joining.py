"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Master and slave behave incredibly peculiar when issuing a signal while
the master joins with the slave thread.

Observations:
- the KeyboardInterrupt is not caught immediately by master, but only after
the slave thread finished all its instructions
- after the join is released, the master thread captures the KeyboardInterrupt
- on Linux the slave thread is still alive after the join, even though it
supposedly ended. On MacOS the slave identifies as dead.
- on Linux when the master thread reaches its end, it will linger forever.
If you do a Ctrl+C while lingering, Python raises a KeyboardInterrupt from
what appears to be an attempt to acquire a lock by the thread.
On MacOS the process terminates right after the last instruction.
"""

import signal
import time
import threading as th


def do_some() -> None:
    print("[SLAVE] ALIVE", flush=True)
    i = 1
    for i in range(10):
        print(f"[SLAVE] LOL {i}", flush=True)
        if i == 2:
            print("\n---> SIGINT FROM SLAVE <---\n")
            signal.raise_signal(signal.SIGINT)

        i += 1
        time.sleep(0.2)

    print("[SLAVE] DEAD", flush=True)


def main() -> None:
    print("MASTER START")

    slave = th.Thread(target=do_some)

    slave.start()

    print("[MASTER] #1 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    try:
        print("[MASTER] JOIN WITH SLAVE ...", flush=True)
        slave.join()
    except KeyboardInterrupt:
        print("[MASTER] SIGINT DETECTED", flush=True)

    print("[MASTER] #2 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    TIMEOUT = 1
    print(
        f"[MASTER] FINAL JOIN WITH SLAVE (timeout {TIMEOUT} seconds) ...",
        flush=True
    )
    slave.join(TIMEOUT)

    print("[MASTER] #3 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    print("MASTER STOP")


if __name__ == "__main__":
    main()
