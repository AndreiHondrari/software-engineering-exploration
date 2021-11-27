import multiprocessing as mp


def do_something() -> None:
    this_process = mp.current_process()

    print(f"[{this_process.name}] START")

    print(f"[{this_process.name}]", '-' * 10)
    print(f"[{this_process.name}] PID: {this_process.pid}")
    print(f"[{this_process.name}]", '-' * 10)

    print(f"[{this_process.name}] STOP")


def main() -> None:
    print("[MAIN] START")

    # create process
    proc = mp.Process(
        target=do_something,
        name="maximus"
    )

    # start process
    proc.start()

    # wait for process to finish
    proc.join()

    print("[MAIN] DONE")


if __name__ == '__main__':
    main()
