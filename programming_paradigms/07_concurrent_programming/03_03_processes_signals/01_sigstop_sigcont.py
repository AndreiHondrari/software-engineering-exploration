import os
import signal
import time
import multiprocessing as mp
from typing import Any


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def do_some(name: str) -> None:
    tprint(f"[SLAVE {name}] START", flush=True)

    i = 1
    try:
        while True:
            tprint(f"[SLAVE {name}] KEK {i}", flush=True)
            i += 1
            time.sleep(0.5)

    except KeyboardInterrupt:
        tprint(f"[SLAVE {name}] SIGINT DETECTED", flush=True)

    tprint(f"[SLAVE {name}] STOP", flush=True)


def main() -> None:
    tprint("[MASTER] ALIVE")

    SLAVE_1_NAME = "Gandalf"
    SLAVE_2_NAME = "Xavier"

    slave_1 = mp.Process(target=do_some, args=(SLAVE_1_NAME,))
    slave_2 = mp.Process(target=do_some, args=(SLAVE_2_NAME,))

    slave_1.start()
    slave_2.start()

    slave_1_state = True
    try:
        while True:
            time.sleep(1)

            if slave_1.ident is None:
                tprint(f"[MASTER] NOTHING ELSE TO DO WITH {SLAVE_1_NAME}")
            else:
                if slave_1_state:
                    print(f"[MASTER] SUSPENDING {SLAVE_1_NAME}")
                    os.kill(slave_1.ident, signal.SIGSTOP)
                else:
                    print(f"[MASTER] RESUMING {SLAVE_1_NAME}")
                    os.kill(slave_1.ident, signal.SIGCONT)

            slave_1_state = not slave_1_state

    except KeyboardInterrupt:
        print()
        tprint("Ctrl+C detected", flush=True)

    if not slave_1_state:
        tprint(f"[MASTER] {SLAVE_1_NAME} IS SUSPENDED. KILLING ...")
        slave_1.kill()

    tprint("[MASTER] FINAL JOIN WITH SLAVES ...")
    slave_1.join()
    slave_2.join()

    tprint("[MASTER] DEAD", flush=True)


if __name__ == "__main__":
    main()
