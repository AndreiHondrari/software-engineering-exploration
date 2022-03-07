"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Master and slave behave incredibly peculiar when issuing a signal while
the master joins with the slave thread.

If a custom sigint handler is specified, and a slave thread raises a SIGINT,
the slave passes the SIGINT to the master thread, but master thread only
queues the SIGINT until the join is finished, and only after the join is
finished does it consider calling the custom sigint handler.

Functionality is consistent between MacOS and Linux. Slave thread exhibits
dead status after the join. Master ends after the last instruction, without
any side-effects
"""

import signal
import time
import threading as th
from types import FrameType


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
