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
any side-effects.

In order to counter-act the "wait until the last moment for SIGINT" when
raising the SIGINT manually from the slave, we will try to loop a timed join
in the master.
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


join_active = True


def sigint_handler(signum: int, frame: FrameType) -> None:
    global join_active
    print("\n---> SIGINT HANDLER CALL <---\n")
    join_active = False


def main() -> None:
    global join_active
    print("MASTER START")

    signal.signal(signal.SIGINT, sigint_handler)

    slave = th.Thread(target=do_some)
    slave.start()

    print("[MASTER] #1 - IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    try:
        print("[MASTER] JOIN WITH SLAVE ...", flush=True)
        while slave.is_alive() and join_active:
            slave.join(0.5)
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
