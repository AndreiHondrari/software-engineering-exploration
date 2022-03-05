"""
Trying to capture KeyboardInterrupt directly in the main seems to have
unforseen consequences for threads.

Observations:
- join no longer works after capturing KeyboardInterrupt even if
  the thread is still running
- the master will just end
- the slave thread will end prematurely
- the slave thread does not seem to capture any exception

This might be an isolated just to the Python ecosystem.

"""

import time
import threading as th

from typing import Any


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def do_some(kill: th.Event) -> None:
    tprint("[SLAVE] ALIVE", flush=True)

    try:
        i = 1
        while not kill.is_set():
            tprint(f"[SLAVE] {i}", flush=True)
            i += 1
            time.sleep(0.5)

        tprint("[SLAVE] I'M DONE ! :'( ", flush=True)

    except Exception as err:
        tprint("[SLAVE] ERR:", repr(err), flush=True)

    COUNTDOWN_LIMIT = 5  # seconds
    tprint(f"[SLAVE] FINAL COUNTDOWN ({COUNTDOWN_LIMIT} seconds)", flush=True)
    time.sleep(COUNTDOWN_LIMIT)

    tprint("[SLAVE] DEAD", flush=True)


def main() -> None:
    tprint("[MASTER] ALIVE", flush=True)

    kill = th.Event()
    slave = th.Thread(target=do_some, args=(kill,))

    slave.start()

    try:
        tprint("[MASTER] JOIN SLAVE")
        slave.join()
    except KeyboardInterrupt:
        print(flush=True)
        tprint("[MASTER] KEYB INT. KILL", flush=True)
        kill.set()

    tprint("[MASTER] WAIT FOR SLAVE TO DIE ...", flush=True)
    slave.join()

    tprint("[MASTER] SLAVE LIVE:", slave.is_alive(), flush=True)

    SLEEP_LIMIT = 1  # seconds
    tprint(f"[MASTER] FINAL SLEEP ({SLEEP_LIMIT} seconds)", flush=True)
    time.sleep(SLEEP_LIMIT)

    tprint("[MASTER] DEAD", flush=True)


if __name__ == "__main__":
    main()
