import threading


def do_something() -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED")

    print(f"[{this_thread.name}] " + '-' * 10)
    print(f"[{this_thread.name}] IDENT: {this_thread.ident}")
    print(f"[{this_thread.name}] NATID: {this_thread.native_id}")
    print(f"[{this_thread.name}] ALIVE: {this_thread.is_alive()}")
    print(f"[{this_thread.name}] DAEMN: {this_thread.daemon}")
    print(f"[{this_thread.name}] " + '-' * 10)


def main() -> None:
    print("MAIN START")

    some_thread = threading.Thread(
        target=do_something,
        name="maximus"
    )

    some_thread.start()

    some_thread.join()

    print("MAIN DONE")


if __name__ == '__main__':
    main()
