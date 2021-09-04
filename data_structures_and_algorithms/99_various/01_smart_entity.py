

class SmartEntity:

    def __init__(self) -> None:
        self.input: int = 0
        self.response: int = 0
        self.state: int = 0

    @property
    def memory(self) -> int:
        return self.state

    def consume(self, x: int) -> None:
        self.input = x

    def reward(self) -> None:
        self.state = self.input


count: int = 1


def do_nonrewarding_action(ent: SmartEntity, param: int) -> None:
    global count
    print(f"#{count} Non-rewarding action", end=" | ")
    ent.consume(param)
    print(f"Entity memory: {ent.memory}")
    count += 1


def do_rewarding_action(ent: SmartEntity, param: int) -> None:
    global count
    print(f"#{count} Rewarding action", end=" | ")
    ent.consume(param)
    ent.reward()
    print(f"Entity memory: {ent.memory}")
    count += 1


if __name__ == '__main__':

    ent = SmartEntity()

    do_nonrewarding_action(ent, 11)
    do_nonrewarding_action(ent, 22)
    do_rewarding_action(ent, 33)
    do_nonrewarding_action(ent, 44)
    do_nonrewarding_action(ent, 55)
    do_rewarding_action(ent, 66)
    do_nonrewarding_action(ent, 77)
    do_nonrewarding_action(ent, 88)
