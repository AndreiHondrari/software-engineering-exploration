import time
import random
import multiprocessing as mp
from multiprocessing.connection import Connection


def do_something(kill_receiver: Connection) -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT ...", flush=True)
    while True:
        # detect kill
        if kill_receiver.poll():
            print(f"[{this_proc.name}] kill detected", flush=True)
            break

        print(f"[{this_proc.name}] DO {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    print(f"[{this_proc.name}] DONE", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    kill_receiver, kill_sender = mp.Pipe(duplex=False)

    some_proc = mp.Process(
        target=do_something,
        name="maximus",
        args=(kill_receiver,)
    )

    some_proc.start()

    print("[MAIN] WAIT 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate kill ...")
    kill_sender.send(None)

    print("[MAIN] wait for process to DIE ...")
    some_proc.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
