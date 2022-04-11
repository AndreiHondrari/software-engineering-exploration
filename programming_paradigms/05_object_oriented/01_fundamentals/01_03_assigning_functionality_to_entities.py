
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

    # Now this function is part of the entity
    def save_to_database(
        self,
    ) -> None:
        # fake save to database for demo purposes
        print(
            f"Saving to database {self.first_name}, {self.last_name}, "
            f"{self.age}, {self.weapons}"
        )


def main() -> None:
    hprint("Variables passed in batches")

    # entitiesbn
    autobot_1 = Autobot(
        "Optimus", "Prime", 1729, [WEAPON_PULSE_RIFLE]
    )

    autobot_2 = Autobot(
        "Rodimus", "Prime", 1455, [WEAPON_PULSE_RIFLE, WEAPON_EMP_BLASTER])

    # use entities
    autobot_1.save_to_database()
    autobot_2.save_to_database()


if __name__ == "__main__":
    main()
