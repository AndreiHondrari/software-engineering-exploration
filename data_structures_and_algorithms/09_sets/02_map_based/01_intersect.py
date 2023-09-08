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

    def intersect(self, other: 'Set') -> 'Set':
        result = Set()
        for k in other._actual_values:
            if k in self._values:
                result.add(k)
        return result


def main() -> None:
    s1 = Set()
    s2 = Set()

    s1.add(11)
    s1.add(22)
    s1.add(33)
    s1.add(44)

    s2.add(22)
    s2.add(77)
    s2.add(44)
    s2.add(88)

    s3 = s1.intersect(s2)

    print("s1 ->", s1)
    print("s2 ->", s2)
    print("s3 ->", s3)


if __name__ == "__main__":
    main()
