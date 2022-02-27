
import functools

from typing import List

hprint = functools.partial(print, "\n#")

WEAPON_PULSE_RIFLE = 1
WEAPON_EMP_BLASTER = 2
WEAPON_ENERGY_TRACKING_ROCKET = 3


def save_to_database(
    first_name: str,
    last_name: str,
    age: int,
    weapons: List[int],
) -> None:
    # fake save to database for demo purposes
    print(
        f"Saving to database "
        f"{first_name}, {last_name}, {age}, {weapons}"
    )


def main() -> None:
    hprint("Variables passed in batches")

    # first entity
    first_name_1 = "Optimus"
    last_name_1 = "Prime"
    age_1 = 1729
    weapons_1 = [
        WEAPON_PULSE_RIFLE,
    ]

    # second entity
    first_name_2 = "Rodimus"
    last_name_2 = "Prime"
    age_2 = 1455
    weapons_2 = [
        WEAPON_PULSE_RIFLE,
        WEAPON_EMP_BLASTER,
    ]

    # use entities
    save_to_database(first_name_1, last_name_1, age_1, weapons_1)
    save_to_database(first_name_2, last_name_2, age_2, weapons_2)


if __name__ == "__main__":
    main()
