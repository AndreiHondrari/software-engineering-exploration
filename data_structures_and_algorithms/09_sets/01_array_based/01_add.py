

class Set:

    def __init__(self):
        self._values = []

    def __str__(self):
        formatted_values = ', '.join(map(str, self._values))
        return "{" + f"{formatted_values}" + "}"

    def add(self, new_value):
        # worst case O(n)
        for x in self._values:
            if new_value == x:
                return

        self._values.append(new_value)


def main() -> None:
    my_set = Set()

    my_set.add(11)
    my_set.add(22)
    my_set.add(11)
    my_set.add(33)

    print(my_set)


if __name__ == "__main__":
    main()
