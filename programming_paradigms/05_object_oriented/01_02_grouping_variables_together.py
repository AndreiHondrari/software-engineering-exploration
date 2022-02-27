
import functools

from typing import List

hprint = functools.partial(print, "\n#")

WEAPON_PULSE_RIFLE = 1
WEAPON_EMP_BLASTER = 2
WEAPON_ENERGY_TRACKING_ROCKET = 3


class Autobot:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        weapons: List[int]
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weapons = weapons


def save_to_database(
    autobot: Autobot
) -> None:
    # fake save to database for demo purposes
    print(
        f"Saving to database {autobot.first_name}, {autobot.last_name}, "
        f"{autobot.age}, {autobot.weapons}"
    )


def main() -> None:
    hprint("Variables passed in batches")

    # entities
    autobot_1 = Autobot(
        "Optimus", "Prime", 1729, [WEAPON_PULSE_RIFLE]
    )

    autobot_2 = Autobot(
        "Rodimus", "Prime", 1455, [WEAPON_PULSE_RIFLE, WEAPON_EMP_BLASTER])

    # use entities
    save_to_database(autobot_1)
    save_to_database(autobot_2)


if __name__ == "__main__":
    main()
