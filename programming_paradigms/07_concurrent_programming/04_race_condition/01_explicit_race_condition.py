import time
import threading


global_variable: int = 11


def do_illegal_race() -> None:
    global global_variable
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] START", flush=True)

    print(f"[{this_thread.name}] wait for 1s", flush=True)
    time.sleep(1)

    print(f"[{this_thread.name}] corrupt the global", flush=True)
    global_variable = 666

    print(f"[{this_thread.name}] STOP", flush=True)


def do_something() -> None:
    global global_variable
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] START", flush=True)

    local_variable: int = 0

    if global_variable < 20:
        print(
            f"[{this_thread.name}] < 20 evaluation for "
            f"not corrupted global {global_variable}",
            flush=True
        )
        print(f"[{this_thread.name}] do some work for 2s ...", flush=True)
        time.sleep(2)

        print(
            f"[{this_thread.name}] use the corrupted global in local",
            flush=True
        )
        local_variable = global_variable

    else:
        print(f"[{this_thread.name}] >= 20", flush=True)
        # whatever ...we don't reach this in this example

    print(
        f"[{this_thread.name}] our corrupted local: {local_variable}",
        flush=True
    )

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START")

    # create threads
    print("[MAIN] create threads")
    illegal_racer_thread = threading.Thread(
        target=do_illegal_race,
        name="criminal"
    )
    some_thread = threading.Thread(
        target=do_something,
        name="maximus"
    )

    # start threads
    print("[MAIN] start threads")
    illegal_racer_thread.start()
    some_thread.start()

    # wait for threads
    print("[MAIN] wait for threads to DIE ....")
    illegal_racer_thread.join()
    some_thread.join()

    print("[MAIN] STOP")


if __name__ == '__main__':
    main()
