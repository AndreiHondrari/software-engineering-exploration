import abc


class StateContext:

    def __init__(self, initial_state: 'State') -> None:
        self._state = initial_state

    def change_state(self, state: 'State') -> None:
        self._state = state


class State(abc.ABC):

    # Non-context-altering methods
    @abc.abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def doing_that(self) -> None:
        raise NotImplementedError

    # Context-altering methods
    @abc.abstractmethod
    def do_something_altering(self, context: StateContext) -> None:
        """
        This method will do something and change context state eventually
        """
        raise NotImplementedError


class StateX(State):
    def do_this(self) -> None:
        print("[SX] doing this")

    def do_that(self) -> None:
        print("[SX] doing that")

    def do_something_altering(self, context: StateContext) -> None:
        print("[SX] doing altering stuff")
