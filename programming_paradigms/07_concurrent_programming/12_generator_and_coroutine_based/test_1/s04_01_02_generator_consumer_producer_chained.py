

VALUES = [1, 3, 5]


def produce():
    for value in VALUES:
        yield value


def add(source_generator, term):
    for value in source_generator:
        yield value + term


def multiply(source_generator, factor):
    for value in source_generator:
        yield value * factor


def consume(source_generator):
    for value in source_generator:
        print("value", value)


def main() -> None:
    p = produce()
    x = add(p, 2)
    y = multiply(x, 10)
    consume(y)


if __name__ == "__main__":
    main()
