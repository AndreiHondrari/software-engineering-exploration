"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Master and slave behave incredibly peculiar when issuing a signal while
the master joins with the slave thread.

MacOS and Linux behaviour when issuing a Ctrl+C or SIGINT from outside of the
process group while joining in the master with the slave thread, will yield
peculiar inconsistent behaviour.

How to experiment:
- run the script (will an infinite loop in the slave thread)
- issue SIGINT or do Ctrl+C

Observations on MacOS:
- slave thread halts immediately,
- master can't join with the slave anymore
- slave identitifes as dead

Observations on Linux:
- slave thread never dies
- master captures the SIGINT immediately
- on secondary SIGINT, master raises exception from a lock acquire function
"""

import time
import threading as th


def do_some() -> None:
    print("[SLAVE] ALIVE", flush=True)
    i = 1
    while True:
        print(f"[SLAVE] LOL {i}", flush=True)
        i += 1
        time.sleep(1)


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
