from typing import Tuple


class Set:

    def __init__(self):
        self._values = {}

    def __str__(self):
        formatted_values = ', '.join(map(str, self._values.keys()))
        return "{" + f"{formatted_values}" + "}"

    @property
    def _actual_values(self) -> Tuple[int]:
        return tuple(self._values.keys())

    def add(self, new_value: int):
        # worst case O(1)
        if new_value not in self._values:
            self._values[new_value] = None


def main() -> None:
    my_set = Set()

    my_set.add(11)
    my_set.add(22)
    my_set.add(11)
    my_set.add(33)

    print(my_set)


if __name__ == "__main__":
    main()
