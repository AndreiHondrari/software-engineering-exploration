from typing import Callable

def do_some(msg1: str, msg2: str) -> None:
    print(f"DO_SOME | {msg1} | {msg2}")


class OperationTypeA:

    def __init__(
        self,
        routine: Callable[[str, str], None],
        y: str
    ) -> None:
        self.routine = routine
        self.y = y

    def __call__(self, x: str) -> None:
        self.routine(self.y, x)


class OperationTypeB:

    def __init__(
        self,
        routine: Callable[[str, str], None],
        y: str
    ) -> None:
        self.routine = routine
        self.y = y

    def __call__(self, x: str) -> None:
        self.routine(x, self.y)


class OperationTypeC:

    def __init__(
        self,
        routine: Callable[[str, str], None],
    ) -> None:
        self.routine = routine

    def __call__(self, x: str) -> None:
        self.routine(x, x)


def main() -> None:
    f1 = OperationTypeA(do_some, "kek")
    f2 = OperationTypeB(do_some, "lol")
    f3 = OperationTypeC(do_some)

    f1("aaa")
    f1("bbb")

    f2("ccc")
    f2("ddd")

    f3("eee")
    f3("fff")


if __name__ == "__main__":
    main()
