"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Master and slave behave incredibly peculiar when issuing a signal while
the master joins with the slave thread.

Specifying a custom sigint handler will stabilise the behaviour while joining
on both Linux and MacOS.

How to test:
- run the script
- try several times to press Ctrl+C

Observations:
- sigint handler captures all Ctrl+C presses
- slave and master thread exit cleanly as expected
- join never releases due to Ctrl+C
"""

import signal
import time
import threading as th
from types import FrameType


def do_some() -> None:
    print("[SLAVE] ALIVE", flush=True)
    i = 1
    for i in range(5):
        print(f"[SLAVE] LOL {i}", flush=True)
        i += 1
        time.sleep(1)


def sigint_handler(signum: int, frame: FrameType) -> None:
    print("\n---> SIGINT HANDLER CALL <---\n")


def main() -> None:
    print("MASTER START")

    signal.signal(signal.SIGINT, sigint_handler)

    slave = th.Thread(target=do_some)

    slave.start()

    print("[MASTER] #1 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    try:
        print("[MASTER] JOIN WITH SLAVE ...", flush=True)
        slave.join()
    except KeyboardInterrupt:
        print("[MASTER] SIGINT DETECTED", flush=True)

    print("[MASTER] #2 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    TIMEOUT = 2
    print(
        f"[MASTER] FINAL JOIN WITH SLAVE (timeout {TIMEOUT} seconds) ...",
        flush=True
    )
    slave.join(TIMEOUT)

    print("[MASTER] #3 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    print("MASTER STOP")


if __name__ == "__main__":
    main()
