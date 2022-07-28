

class SomeOperation:

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __call__(self) -> None:
        print(self.msg)


def main() -> None:
    op1 = SomeOperation("DO_THIS")
    op2 = SomeOperation("DO_THAT")

    op1()
    op1()

    op2()
    op2()


if __name__ == "__main__":
    main()
