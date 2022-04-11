

class A:

    def __init__(self) -> None:
        self.x = 11
        self.y = 1111


class B(A):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name

    def do_something(self) -> None:
        self.x *= 2
        self.y *= 2


if __name__ == '__main__':
    o1 = B("Luigi")

    o1.do_something()

    print(f"{o1.x} {o1.y}")
