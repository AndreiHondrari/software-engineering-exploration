
import functools
from typing import List

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Search first character")
    s1 = "aaabcckeeefffgghhhiiiikjjjjlllmmoopppkkrrrrssstttuuuvvxxk"
    TARGET = 'k'

    print("Input :", s1)
    print("Target: ", TARGET)

    positions: List[int] = []

    for i in range(len(s1)):
        if s1[i] == TARGET:
            positions.append(i)

    if len(positions) == 0:
        print("Nothing found")
    else:
        print("Found at:", positions)


if __name__ == "__main__":
    main()
