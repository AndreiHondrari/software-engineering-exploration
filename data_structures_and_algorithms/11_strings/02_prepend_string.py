
import functools

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Prepend string")
    s1 = "abc"
    print("Before :", s1)

    s2 = "xyz" + s1
    print("After  :", s2)


if __name__ == "__main__":
    main()
