import abc


class AbstractComponent(abc.ABC):

    @abc.abstractmethod
    def do_operation_1(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def do_operation_2(self) -> None:
        raise NotImplementedError

    def do(self) -> None:
        self.do_operation_1()
        self.do_operation_2()


class ConcreteComponentX(AbstractComponent):

    def do_operation_1(self) -> None:
        print("[CCX] doing 1")

    def do_operation_2(self) -> None:
        print("[CCX] doing 2")


class ConcreteComponentY(AbstractComponent):

    def do_operation_1(self) -> None:
        print("[CCY] doing 1")

    def do_operation_2(self) -> None:
        print("[CCY] doing 2")


if __name__ == '__main__':
    print("# Doing as X")
    object1 = ConcreteComponentX()
    object1.do()

    print("\n# Doing as Y")
    object2 = ConcreteComponentY()
    object2.do()
