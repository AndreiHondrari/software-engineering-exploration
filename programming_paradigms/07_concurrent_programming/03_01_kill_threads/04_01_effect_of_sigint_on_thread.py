"""
Signals caught by any thread are always passed to the root of the
process group, particularly the main thread.

Calling pthread kill with SIGINT on a slave thread, will just make the slave
pass this SIGINT to master, which will have to deal with somehow.

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
            i += 1
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("[SLAVE] SIGINT DETECTED", flush=True)

    print("[SLAVE] DEAD", flush=True)


def main() -> None:
    print("MASTER START")

    master = th.main_thread()
    slave = th.Thread(target=do_some)

    slave.start()

    i = 1
    running = True
    while running:
        print(f"[MASTER] KEK {i}", flush=True)
        print("[MASTER] IS SLAVE ALIVE?:", slave.is_alive(), flush=True)

        try:
            if i == 2:
                print("\n--> SIGINT TO SLAVE <--\n", flush=True)
                if master.ident is None:
                    print("[MASTER] ABNORMAL MISSING IDENTITY FOR M-THREAD")
                else:
                    signal.pthread_kill(master.ident, signal.SIGINT)

        except KeyboardInterrupt:
            print("[MASTER] SIGINT DETECTED", flush=True)
            running = False

        print(
            "[MASTER] IS SLAVE ALIVE (FINAL)?:",
            slave.is_alive(),
            flush=True
        )

        time.sleep(0.2)

        i += 1

    print("MASTER STOP")


if __name__ == "__main__":
    main()
