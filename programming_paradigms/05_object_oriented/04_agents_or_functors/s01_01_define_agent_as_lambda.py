from typing import Callable


def do_some(msg1: str, msg2: str) -> None:
    print(f"DO_SOME | {msg1} | {msg2}")


def main() -> None:
    f1: Callable[[str], None] = lambda x: do_some("kek", x)
    f2: Callable[[str], None] = lambda x: do_some(x, "lol")
    f3: Callable[[str], None] = lambda x: do_some(x, x)

    f1("aaa")
    f1("bbb")

    f2("ccc")
    f2("ddd")

    f3("eee")
    f3("fff")


if __name__ == "__main__":
    main()
