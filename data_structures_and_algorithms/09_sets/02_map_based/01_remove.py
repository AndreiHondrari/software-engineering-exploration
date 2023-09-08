

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

    def remove(self, value):

        # worst case O(n)
        for i in range(len(self._values)):
            if value == self._values[i]:
                self._values = self._values[:i] + self._values[i+1:]
                break


def main() -> None:
    my_set = Set()

    my_set.add(11)
    my_set.add(22)
    my_set.add(11)
    my_set.add(33)

    my_set.remove(22)

    my_set.add(900)
    my_set.add(911)
    my_set.add(922)
    my_set.add(933)
    my_set.add(955)
    my_set.add(966)

    my_set.remove(922)
    my_set.remove(955)

    print(my_set)


if __name__ == "__main__":
    main()
