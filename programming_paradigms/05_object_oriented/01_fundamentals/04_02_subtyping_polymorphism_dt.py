
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


def print_name(obj: Thing) -> None:
    print(f"object's name: {obj.get_name()}")


def main() -> None:

    a = A("Maximus Prime")
    b = B("Gandalf", "Greybeard")

    print_name(a)
    print_name(b)


if __name__ == "__main__":
    main()
