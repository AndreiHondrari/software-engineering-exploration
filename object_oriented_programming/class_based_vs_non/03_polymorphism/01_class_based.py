import abc


class Base(abc.ABC):

    def __init__(self) -> None:
        self.x = 111

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class A(Base):

    def do_something(self) -> None:
        self.x *= 5


class B(Base):

    def do_something(self) -> None:
        self.x *= 7


def f1(obj: Base) -> None:
    obj.do_something()


if __name__ == '__main__':

    o1 = A()
    o2 = B()

    f1(o1)
    f1(o2)

    print(f"{o1.x} {o2.x}")
