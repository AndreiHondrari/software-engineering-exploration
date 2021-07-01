import abc


class Strategy(abc.ABC):

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class Context:

    def __init__(self, initial_strategy: Strategy):
        self._strategy = initial_strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do(self) -> None:
        print("Context doing")
        self._strategy.do_something()


class ConcreteStrategyA(Strategy):

    def do_something(self) -> None:
        print(f"[CSA] [{self.name}] doing")


class ConcreteStrategyB(Strategy):

    def do_something(self) -> None:
        print(f"[CSB] [{self.name}] doing")


if __name__ == '__main__':
    strategy1 = ConcreteStrategyA("Jeff")
    strategy2 = ConcreteStrategyB("Xavier")
    strategy3 = ConcreteStrategyA("Severus")

    context = Context(strategy1)

    print("# First strategy")
    context.do()

    print("\n# Second strategy")
    context.set_strategy(strategy2)
    context.do()

    print("\n# Third strategy")
    context.set_strategy(strategy3)
    context.do()
