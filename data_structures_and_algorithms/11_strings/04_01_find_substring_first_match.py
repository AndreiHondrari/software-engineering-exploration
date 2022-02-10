
import functools
from typing import Optional

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Search first character")
    s1 = "ab X cd XY efg XYZ hijkl XYZ mnopqrst"
    TARGET = 'XYZ'

    print("Input :", s1)
    print("Target: ", TARGET)

    pos: Optional[int] = None

    for i in range(len(s1)):
        match = True
        for j in range(len(TARGET)):
            if s1[i + j] != TARGET[j]:
                match = False
                break

        if match:
            pos = i
            break

    if pos is None:
        print("Nothing found")
    else:
        print(f"Found at {pos}")


if __name__ == "__main__":
    main()
