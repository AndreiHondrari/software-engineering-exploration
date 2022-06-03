

GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


def binnet_nth(n: int) -> int:
    return int(
        (GOLDEN_RATIO ** n - (-GOLDEN_RATIO) ** (-n)) /
        (5 ** 0.5)
    )


def main() -> None:
    t = list(range(1, 45 + 1))

    for x in t:
        y = binnet_nth(x)
        print(x, "->", y)


if __name__ == "__main__":
    main()
