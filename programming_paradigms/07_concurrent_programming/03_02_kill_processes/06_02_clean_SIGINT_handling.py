import time
import signal
import multiprocessing as mp

from types import FrameType
from typing import Any


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def do_some(kill: mp.Event, name: str) -> None:
    tprint(f"[SLAVE {name}] ALIVE")

    # this is absolutely necessary
    # so that our child processes don't act on the SIGINT
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    try:
        i = 1
        while not kill.is_set():
            tprint(f"[SLAVE {name}] {i}", flush=True)
            i += 1
            time.sleep(0.5)
        tprint(f"[SLAVE {name}] I'M DONE ! :'( ")

    # this will not be triggered ever because of SIG_IGN above
    except KeyboardInterrupt:
        tprint(f"[SLAVE {name}] SIGINT detected", flush=True)

    except Exception as err:
        tprint(f"[SLAVE {name}] ERR:", repr(err), flush=True)

    COUNTDOWN_LIMIT = 3  # seconds
    tprint(
        f"[SLAVE {name}] FINAL COUNTDOWN ({COUNTDOWN_LIMIT} seconds)",
        flush=True
    )
    time.sleep(5)

    tprint(f"[SLAVE {name}] DEAD", flush=True)


def main() -> None:
    tprint("[MASTER] ALIVE")

    kill = mp.Event()
    SLAVE_1_NAME = "Gandalf"
    SLAVE_2_NAME = "Xavier"

    slave_1 = mp.Process(target=do_some, args=(kill, "Gandalf"))
    slave_2 = mp.Process(target=do_some, args=(kill, "Xavier"))

    slave_1.start()
    slave_2.start()

    def sigint_handle(signum: int, frame: FrameType) -> None:
        print(flush=True)
        tprint("[MASTER] KEYB INT. KILL", flush=True)
        kill.set()

    tprint("[MASTER] REGISTER SIGINT HANDLER")
    signal.signal(signal.SIGINT, sigint_handle)

    tprint(f"[MASTER] S {SLAVE_1_NAME} LIVE:", slave_1.is_alive(), flush=True)
    tprint(f"[MASTER] S {SLAVE_2_NAME} LIVE:", slave_2.is_alive(), flush=True)

    tprint("[MASTER] JOIN SLAVES")
    slave_1.join()
    slave_2.join()

    tprint(f"[MASTER] S {SLAVE_1_NAME} LIVE:", slave_1.is_alive(), flush=True)
    tprint(f"[MASTER] S {SLAVE_2_NAME} LIVE:", slave_2.is_alive(), flush=True)

    SLEEP_LIMIT = 1  # seconds
    tprint(f"[MASTER] FINAL SLEEP ({SLEEP_LIMIT} seconds)", flush=True)
    time.sleep(SLEEP_LIMIT)

    tprint("[MASTER] DEAD", flush=True)


if __name__ == "__main__":
    main()
