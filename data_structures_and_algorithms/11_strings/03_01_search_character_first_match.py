
import functools
from typing import Optional

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Search first character")
    s1 = "abcdefghijklmnopqrst"
    TARGET = 'k'

    print("Input :", s1)
    print("Target: ", TARGET)

    pos: Optional[int] = None

    for i in range(len(s1)):
        if s1[i] == TARGET:
            pos = i
            break

    if pos is None:
        print("Nothing found")
    else:
        print(f"Found at {pos}")


if __name__ == "__main__":
    main()
