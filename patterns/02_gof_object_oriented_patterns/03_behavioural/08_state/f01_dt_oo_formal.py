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
    def do_that(self) -> None:
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
        context.change_state(StateY())


class StateY(State):
    def do_this(self) -> None:
        print("[SY] doing this")

    def do_that(self) -> None:
        print("[SY] doing that")

    def do_something_altering(self, context: StateContext) -> None:
        print("[SY] doing altering stuff")
        context.change_state(StateX())


class ConcreteContext(StateContext):

    def foo(self) -> None:
        print("Fooing")
        self._state.do_this()
        self._state.do_that()

    def bar(self) -> None:
        print("Baring")
        self._state.do_something_altering(self)


if __name__ == '__main__':
    initial_state = StateX()
    context = ConcreteContext(initial_state)
    # from state X
    context.foo()
    context.bar()  # switches state to Y

    # from state Y
    context.foo()
    context.bar()  # switches state to X

    # from state X
    context.foo()
