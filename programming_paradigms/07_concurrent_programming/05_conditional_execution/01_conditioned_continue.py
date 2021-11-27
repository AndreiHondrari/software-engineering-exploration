import time
import threading


def do_something(some_condition: threading.Condition) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] wait for condition ...", flush=True)
    some_condition.acquire()
    some_condition.wait()
    some_condition.release()

    print(f"[{tname}] condition passed!", flush=True)

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START")

    some_condition = threading.Condition()

    print("[MAIN] create thread")
    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(some_condition,)
    )

    print("[MAIN] start thread")
    some_thread.start()

    print("[MAIN] wait 2s ...")
    time.sleep(2)

    print("[MAIN] signal continue")
    some_condition.acquire()
    some_condition.notify()
    some_condition.release()

    print("[MAIN] wait for thread to finish")
    some_thread.join()

    print("[MAIN] STOP")


if __name__ == '__main__':
    main()
