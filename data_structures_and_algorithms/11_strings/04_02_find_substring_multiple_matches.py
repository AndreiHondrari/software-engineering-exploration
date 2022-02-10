
import functools
from typing import List

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Search first character")
    s1 = "ab X cd XY efg XYZ hijkl XYZ mnopqrst"
    TARGET = 'XYZ'

    print("Input :", s1)
    print("Target: ", TARGET)

    positions: List[int] = []

    for i in range(len(s1)):
        match = True
        for j in range(len(TARGET)):
            if s1[i + j] != TARGET[j]:
                match = False
                break

        if match:
            positions.append(i)

    if len(positions) == 0:
        print("Nothing found")
    else:
        print("Found at:", positions)


if __name__ == "__main__":
    main()
