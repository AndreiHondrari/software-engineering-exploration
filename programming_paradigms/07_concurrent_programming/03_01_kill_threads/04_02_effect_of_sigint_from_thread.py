"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Raising a signal from inside a slave thread will force this slave to pass a
SIGINT to the master thread.

The slave thread never captures signals.
"""

import signal
import time
import threading as th


def do_some() -> None:
    try:
        print("[SLAVE] ALIVE", flush=True)
        i = 1
        for i in range(10):
            print(f"[SLAVE] LOL {i}", flush=True)
            if i == 2:
                print("\n---> SIGINT FROM SLAVE <---\n")
                signal.raise_signal(signal.SIGINT)

            i += 1
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("[SLAVE] SIGINT DETECTED", flush=True)

    print("[SLAVE] DEAD", flush=True)


def main() -> None:
    print("MASTER START")

    slave = th.Thread(target=do_some)

    slave.start()

    i = 1
    running = True
    try:
        while running:
            print(f"[MASTER] KEK {i}", flush=True)
            print("[MASTER] IS SLAVE ALIVE?:", slave.is_alive(), flush=True)
            time.sleep(0.5)
            i += 1

    except KeyboardInterrupt:
        print("[MASTER] SIGINT DETECTED", flush=True)

    print("[MASTER] IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

    print("MASTER STOP")


if __name__ == "__main__":
    main()
