

class A:
    def __init__(self, name: str) -> None:
        self.name = name

    def do_this(self) -> None:
        print(f"[A] {self.name} DO_THIS")


class B:
    def __init__(self, name: str) -> None:
        self.name = name
        self.a = A("Gandalf")

    def do_some(self) -> None:
        print(f"[B] {self.name} calls {self.a.name}")
        self.a.do_this()


def main() -> None:
    b1 = B("Jimmy")
    b2 = B("Jeff")

    b1.do_some()
    b2.do_some()


if __name__ == "__main__":
    main()
