
import abc


class Thing(abc.ABC):

    @abc.abstractmethod
    def get_name(self) -> str:
        pass


class A(Thing):

    def __init__(self, full_name: str) -> None:
        self._full_name = full_name

    def get_name(self) -> str:
        return self._full_name


class B(Thing):

    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name

    def get_name(self) -> str:
        return f"{self._first_name} {self._last_name}"


def main() -> None:

    a = A("Maximus Prime")
    name_1: str = a.get_name()
    print(f"a's name: {name_1}")

    b = B("Gandalf", "Greybeard")
    name_2: str = b.get_name()
    print(f"b's name: {name_2}")


if __name__ == "__main__":
    main()
