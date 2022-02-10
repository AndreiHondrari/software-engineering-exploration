
import functools

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Prepend character")
    s1 = "abc"
    print("Before :", s1)

    s2 = "x" + s1
    print("After  :", s2)


if __name__ == "__main__":
    main()
